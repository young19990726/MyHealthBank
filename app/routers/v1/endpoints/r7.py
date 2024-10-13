import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import R7, FexreportR7, OrderCodeMasterR1, CureRecR1
from app.schemas.v1.r7 import R7Base 


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error') 


## [GET]：Root#
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")} 


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=R7Base, name="Post r7", description="Post r7", include_in_schema=True)
async def post_r7(
    db: Session = Depends(get_conn)
    ):

    try:
        fexreport_data = db.query(FexreportR7).filter(FexreportR7.is_analyzed == False).all()

        if fexreport_data:
            accession_numbers = [f.fk_accession_number for f in fexreport_data]
            cure_rec_data = db.query(CureRecR1).filter(CureRecR1.accession_number.in_(accession_numbers)).all()

            if cure_rec_data:
                cure_rec_dict = {c.accession_number: [] for c in cure_rec_data}
                
                for c in cure_rec_data:
                    cure_rec_dict[c.accession_number].append(c)

                hos_ordercodes = [c.fk_hos_ordercode for c in cure_rec_data]

                order_code_master_data = db.query(OrderCodeMasterR1).filter(OrderCodeMasterR1.hos_ordercode.in_(hos_ordercodes)).all()

                if order_code_master_data:
                    order_code_dict = {o.hos_ordercode: o.order_code for o in order_code_master_data}

                    merged_data = []

                    for fexreport in fexreport_data:

                        order_codes = []  # 用來存放該 accession_number 找到的所有 order_code

                        if fexreport.fk_accession_number in cure_rec_dict:
                            for cure_rec in cure_rec_dict[fexreport.fk_accession_number]:
                                order_code = order_code_dict.get(cure_rec.fk_hos_ordercode)
                                if order_code and order_code not in order_codes:
                                    order_codes.append(order_code)

                        if order_codes:
                            fexreport_order_code = ",".join(order_codes)

                            model = R7(
                                hos=fexreport.hos,
                                cno=fexreport.cno,
                                report_date=fexreport.report_date,
                                fk_accession_number=fexreport.fk_accession_number,
                                ordclnm_name=fexreport.ordclnm_name,
                                data=fexreport.data,
                                order_code=fexreport_order_code,  
                            )
                            merged_data.append(model)

                            fexreport.is_analyzed = True

                    if merged_data:
                        db.add_all(merged_data)
                        db.commit() 

        return {"detail": "Data merged and stored successfully."}

    except IntegrityError as e:
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=400, detail="Integrity error with the provided data")

    except Exception as e:
        db.rollback()
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=500, detail="Error post r7")


## [GET]：
@router.get("", response_model=List[R7Base], name="Get r7", description="Get r7", include_in_schema=True)
async def get_r7(
    cno:str=Query(..., description="CNO"),
    db:Session=Depends(get_conn)
    ):

    try:
        data = db.query(R7).filter(R7.cno == cno).all()

    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=500, detail="Error get r7")
        
    if len(data) == 0:
        raise HTTPException(status_code=404, detail=f"R7Base not exists")
        
    return data