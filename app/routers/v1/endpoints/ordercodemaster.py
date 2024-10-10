import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.requests import Request
from typing import List

from app.database.healthbank import get_conn  
from app.middleware.exception import exception_message  
from app.models.healthbank import OrderCodeMasterR1  
from app.schemas.v1.r1_ordercodemaster import OrderCodeMasterR1Base  


router = APIRouter()


uvicorn_logger = logging.getLogger('uvicorn.error')  
system_logger = logging.getLogger('custom.error')  


# ## [GET]：Root
# @router.get("")
# async def root(request: Request):
#     return {"Root": request.scope.get("root_path")}  


##### 連接資料庫並處理請求 #####
## [POST] : 
@router.post("", response_model=OrderCodeMasterR1Base, name="Post ordercodemaster", description="Post ordercodemaster", include_in_schema=True)
async def post_order_code_master(
    data: OrderCodeMasterR1Base, 
    db: Session = Depends(get_conn)
    ):

    try:
        model = OrderCodeMasterR1(
            hos=data.hos,
            hos_ordercode=data.hos_ordercode,
            order_code=data.order_code
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
        raise HTTPException(status_code=500, detail="Error post ordercodemaster") 


## [GET] : 
@router.get("", response_model=List[OrderCodeMasterR1Base], name="Get ordercodemaster", description="Get ordercodemaster", include_in_schema=True)
async def get_order_code_master(
    skip: int = 0,    # 跳過的資料筆數，預設為 0
    limit: int = 10,  # 每次返回的資料筆數，預設為 10
    db: Session = Depends(get_conn)  
    ):

    try:
        # 使用 offset 和 limit 來分頁查詢資料庫
        data = db.query(OrderCodeMasterR1).offset(skip).limit(limit).all()  # 跳過 skip 筆，取得 limit 筆資料
    
    except Exception as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=500, detail="Error get ordercodemaster")  
    
    if len(data) == 0:
        raise HTTPException(status_code=404, detail="OrderCodeMasterR1 not exists")
    
    return data  