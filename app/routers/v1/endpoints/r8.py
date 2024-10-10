import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import R8, OrderCodeMasterR1, FxyreportR8
from app.schemas.v1.r8 import R8Base 


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error') 


## [GET]：Root#
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")} 


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=R8Base, name="Post r8", description="Post r8", include_in_schema=True)
async def post_r8(
    db: Session = Depends(get_conn)  
):
    try:
        order_code_master_data = db.query(OrderCodeMasterR1).all()
        fxyreport_data = db.query(FxyreportR8).filter(FxyreportR8.is_analyzed == False).all()

        merged_data = []

        for fxyreport in fxyreport_data:
            for order_code_master in order_code_master_data:
                if fxyreport.fk_hos_ordercode == order_code_master.hos_ordercode:  
                    merged_row = R8(
                        hos=fxyreport.hos,
                        cno=fxyreport.cno,
                        performed_start_date=fxyreport.performed_start_date,
                        order_code=order_code_master.order_code,
                        report_text=fxyreport.report_text
                    )
                    merged_data.append(merged_row)

        if merged_data:
            db.add_all(merged_data)  # 只有在有合併資料時才執行
            for fxyreport in fxyreport_data:
                fxyreport.is_analyzed = True
            db.commit()  # 單一提交

        return {"detail": "Data merged and stored successfully."}  # 返回成功訊息

    except IntegrityError as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=400, detail="Integrity error with the provided data") 

    except Exception as e:
        db.rollback()  # 異常時回滾
        system_logger.error(exception_message(e)) 
        raise HTTPException(status_code=500, detail="Error post r8") 

## [GET]：
@router.get("", response_model=List[R8Base], name="Get r8", description="Get r8", include_in_schema=True)
async def get_r8(
    cno:str=Query(..., description="CNO"),
    db:Session=Depends(get_conn)
    ):

    try:
        data = db.query(R8).filter(R8.cno == cno).all()

    except Exception as e:
        system_logger.error(exception_message(e))
        raise HTTPException(status_code=500, detail="Error get r8")
        
    if len(data) == 0:
        raise HTTPException(status_code=404, detail=f"R8Base not exists")
        
    return data