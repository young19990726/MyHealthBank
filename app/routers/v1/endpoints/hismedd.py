import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import HISMEDDR2 
from app.schemas.v1.r2_hismedd import HISMEDDR2Base 


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error') 


## [GET]：Root#
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")} 


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=HISMEDDR2Base, name="Post hismedd", description="Post hismedd", include_in_schema=True)
async def post_hismedd(
    data: HISMEDDR2Base,  
    db: Session = Depends(get_conn)  
    ):

    try:
        model = HISMEDDR2(
            hos=data.hos,
            medno=data.medno,
            cno=data.cno
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
        raise HTTPException(status_code=500, detail="Error post hismedd")  


## [GET] : 
@router.get("", response_model=List[HISMEDDR2Base], name="Get hismedd", description="Get hismedd", include_in_schema=True)
async def get_hismedd(
    skip: int = 0,    # 跳過的資料筆數，預設為 0
    limit: int = 10,  # 每次返回的資料筆數，預設為 10
    db: Session = Depends(get_conn)  
    ):
    
    try:
        # 使用 offset 和 limit 來分頁查詢資料庫
        data = db.query(HISMEDDR2).offset(skip).limit(limit).all()  # 跳過 skip 筆，取得 limit 筆資料
    
    except Exception as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=500, detail="Error get hismedd")  
    
    if len(data) == 0:
        raise HTTPException(status_code=404, detail="HISMEDDR2Base not exists")
    
    return data 