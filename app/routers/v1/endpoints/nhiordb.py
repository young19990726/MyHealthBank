import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import NHIORDBR2 
from app.schemas.v1.r2_nhiordb import NHIORDBR2Base 


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error') 


## [GET]：Root#
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")} 


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=NHIORDBR2Base, name="Post nhiordb", description="Post nhiordb", include_in_schema=True)
async def post_nhiordb(
    data: NHIORDBR2Base,  
    db: Session = Depends(get_conn)  
    ):

    try:
        model = NHIORDBR2(
            hos=data.hos,
            fk_medno=data.fk_medno,
            accession_number=data.accession_number,
            execution_date=data.execution_date,
            expiration_date=data.expiration_date,
            order_code=data.order_code,
            total_number=data.total_number
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
        raise HTTPException(status_code=500, detail="Error post nhiordb")  


## [GET] : 
@router.get("", response_model=List[NHIORDBR2Base], name="Get nhiordb", description="Get nhiordb", include_in_schema=True)
async def get_nhiordb(
    skip: int = 0,    # 跳過的資料筆數，預設為 0
    limit: int = 10,  # 每次返回的資料筆數，預設為 10
    db: Session = Depends(get_conn)  
    ):
    
    try:
        # 使用 offset 和 limit 來分頁查詢資料庫
        data = db.query(NHIORDBR2).offset(skip).limit(limit).all()  # 跳過 skip 筆，取得 limit 筆資料
    
    except Exception as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=500, detail="Error get nhiordb")  
    
    if len(data) == 0:
        raise HTTPException(status_code=404, detail="NHIORDBR2Base not exists")
    
    return data 