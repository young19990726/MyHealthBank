import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import ORDFAR1 
from app.schemas.v1.r1_ordfa import ORDFAR1Base 


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error') 


## [GET]：Root#
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")} 


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=ORDFAR1Base, name="Post ordfa", description="Post ordfa", include_in_schema=True)
async def post_ordfa(
    data: ORDFAR1Base,  
    db: Session = Depends(get_conn)  
    ):

    try:
        model = ORDFAR1(
            hos=data.hos,
            fk_dtlid=data.fk_dtlid,
            order_code=data.order_code,
            total_number=data.total_number,
            dose_day=data.dose_day
            ) 
        db.add(model)  
        db.commit() 
        db.refresh(model) 
        return model 

    except IntegrityError as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=400, detail="Integrity error with the provided data") 

    except Exception as e:
        db.rollback()  
        system_logger.error(exception_message(e)) 
        raise HTTPException(status_code=500, detail="Error post ordfa")  


## [GET] : 
@router.get("", response_model=List[ORDFAR1Base], name="Get ordfa", description="Get ordfa", include_in_schema=True)
async def get_ordfa(
    skip: int = 0,    # 跳過的資料筆數，預設為 0
    limit: int = 10,  # 每次返回的資料筆數，預設為 10
    db: Session = Depends(get_conn)  
    ):
    
    try:
        # 使用 offset 和 limit 來分頁查詢資料庫
        data = db.query(ORDFAR1).offset(skip).limit(limit).all()  # 跳過 skip 筆，取得 limit 筆資料
    
    except Exception as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=500, detail="Error get ordfa")  
    
    if len(data) == 0:
        raise HTTPException(status_code=404, detail="ORDFAR1Base not exists")
    
    return data 