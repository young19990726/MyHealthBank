import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import R2, HISMEDDR2, NHIDTLBR2, NHIORDBR2
from app.schemas.v1.r2 import R2Base 


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error') 


## [GET]：Root#
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")} 


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=R2Base, name="Post r2", description="Post r2", include_in_schema=True)
async def post_r2(
    db: Session = Depends(get_conn)
):
    try:
        dtlb_data = db.query(NHIDTLBR2).filter(NHIDTLBR2.is_analyzed == False).all()

        if dtlb_data:
            fk_mednos = [dtlb.fk_medno for dtlb in dtlb_data] 
            hismedd_data = db.query(HISMEDDR2).filter(HISMEDDR2.medno.in_(fk_mednos)).all()

            if hismedd_data:
                accession_numbers = [dtlb.accession_number for dtlb in dtlb_data]
                ordb_data = db.query(NHIORDBR2).filter(NHIORDBR2.accession_number.in_(accession_numbers)).all()

                if ordb_data:
                    # 建立索引，加速後續的查找
                    hismedd_index = {h.medno: h for h in hismedd_data}
                    ordb_index = {o.accession_number: [] for o in ordb_data}
                    for o in ordb_data: 
                        ordb_index[o.accession_number].append(o)

                    merged_data = []

                    for dtlb in dtlb_data:
                        hismedd = hismedd_index.get(dtlb.fk_medno)
                        if hismedd: 
                            cno = hismedd.cno
                            ordbs = ordb_index.get(dtlb.accession_number)
                            if ordbs:
                                for ordb in ordbs:
                                    merged_record = R2(
                                        hos=dtlb.hos,
                                        cno=cno,
                                        fk_medno=dtlb.fk_medno,
                                        admission_date=dtlb.admission_date,
                                        discharge_date=dtlb.discharge_date,
                                        cm_code=dtlb.cm_code,
                                        pcs_code=dtlb.pcs_code,
                                        execution_date=ordb.execution_date,
                                        expiration_date=ordb.expiration_date,
                                        order_code=ordb.order_code,
                                        total_number=ordb.total_number,
                                        accession_number=ordb.accession_number
                                    )
                                    merged_data.append(merged_record)
                                    ordb.is_analyzed = True

                        dtlb.is_analyzed = True

        if merged_data:
            db.add_all(merged_data)
            db.commit()

        return {"message": "Data merged successfully"}

    except Exception as e:
        system_logger.error(exception_message(e))
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating BasicReport record")


## [GET]：
@router.get("", response_model=List[R2Base], name="Get r2", description="Get r2", include_in_schema=True)
async def get_r2(
    cno:str=Query(..., description="CNO"),
    db:Session=Depends(get_conn)
    ):

    try:
        data = db.query(R2).filter(R2.cno == cno).all()

    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=500, detail="Error get r2")
        
    if len(data) == 0:
        raise HTTPException(status_code=404, detail=f"R2Base not exists")
        
    return data