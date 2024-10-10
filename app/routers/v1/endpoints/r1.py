import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import R1, DTLFAR1, ORDFAR1
from app.schemas.v1.r1 import R1Base 


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error') 


## [GET]：Root#
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")} 


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=R1Base, name="Post r1", description="Post r1", include_in_schema=True)
async def post_r1(
    db: Session = Depends(get_conn)  
):
    try:
        dtlfa_data = db.query(DTLFAR1).filter(DTLFAR1.is_analyzed == False).all()
        ordfa_data = db.query(ORDFAR1).filter(ORDFAR1.is_analyzed == False).all()

        merged_data = []

        for dtlfa in dtlfa_data:
            for ordfa in ordfa_data:
                if dtlfa.dtlid == ordfa.fk_dtlid:  
                    merged_row = R1(
                        hos=dtlfa.hos,
                        dtlid=dtlfa.dtlid,
                        cno=dtlfa.cno,
                        treatment_date=dtlfa.treatment_date,
                        cm_code=dtlfa.cm_code,
                        pcs_code=dtlfa.pcs_code,  
                        order_code=ordfa.order_code,
                        total_number=ordfa.total_number,
                        dose_day=ordfa.dose_day,
                    )
                    merged_data.append(merged_row)

        if merged_data:
            db.add_all(merged_data)  # 只有在有合併資料時才執行
            for dtlfa in dtlfa_data:
                dtlfa.is_analyzed = True
            for ordfa in ordfa_data:
                ordfa.is_analyzed = True
            db.commit()  # 單一提交

        return {"detail": "Data merged and stored successfully."}  # 返回成功訊息

    except IntegrityError as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=400, detail="Integrity error with the provided data") 

    except Exception as e:
        db.rollback()  # 異常時回滾
        system_logger.error(exception_message(e)) 
        raise HTTPException(status_code=500, detail="Error post r1") 

## [GET]：
@router.get("", response_model=List[R1Base], name="Get r1", description="Get r1", include_in_schema=True)
async def get_r1(
    cno:str=Query(..., description="CNO"),
    db:Session=Depends(get_conn)
    ):

    try:
        data = db.query(R1).filter(R1.cno == cno).all()

    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=500, detail="Error get r1")
        
    if len(data) == 0:
        raise HTTPException(status_code=404, detail=f"R1Base not exists")
        
    return data