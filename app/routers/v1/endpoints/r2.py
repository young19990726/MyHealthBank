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
# @router.post("", response_model=R2Base, name="Post r2", description="Post r2", include_in_schema=True)
# async def post_r2(
#     db: Session = Depends(get_conn)  
# ):
#     try:
#         dtlb_data = db.query(NHIDTLBR2).filter(NHIDTLBR2.is_analyzed == False).all()


#         merged_data = []

#         for dtlb in dtlb_data:

#             hismedd_data = db.query(HISMEDDR2).filter(HISMEDDR2.medno == dtlb.fk_medno).all()

#             cno = hismedd_data[0].cno if hismedd_data else None

#             if cno:
#                 # 查詢 NHIORDBR2
#                 ordb_data = db.query(NHIORDBR2).filter(NHIORDBR2.accession_number == dtlb.accession_number).all()

#                 for ordb in ordb_data:  # 使用 ordb_data 而不是 nhiordb_data
#                     merged_record = {
#                         "hos": dtlb.hos,
#                         "cno": cno,
#                         "fk_medno": dtlb.fk_medno,
#                         "admission_date": dtlb.admission_date,
#                         "discharge_date": dtlb.discharge_date,
#                         "cm_code": dtlb.cm_code,
#                         "pcs_code": dtlb.pcs_code,
#                         "execution_date": ordb.execution_date,
#                         "expiration_date": ordb.expiration_date,
#                         "order_code": ordb.order_code,
#                         "total_number": ordb.total_number
#                     }
                    

#                     merged_data.append(merged_record)
#         print(merged_data)

#         # 提交資料變更
#         # for dtlb in dtlb_data:
#         #     dtlb.is_analyzed = True  # 標記為已分析
#         if merged_data:
#             db.add_all(merged_data)
#             db.commit()

#         return {"message": "Data merged successfully"}

#     except Exception as e:
#         system_logger.error(exception_message(e))
#         # db.rollback()  # 確保在出錯時回滾
#         raise HTTPException(status_code=500, detail="Error create BasicReport record")
@router.post("", response_model=R2Base, name="Post r2", description="Post r2", include_in_schema=True)
async def post_r2(
    db: Session = Depends(get_conn)  
):
    try:
        dtlb_data = db.query(NHIDTLBR2).filter(NHIDTLBR2.is_analyzed == False).all()

        merged_data = []

        for dtlb in dtlb_data:
            hismedd_data = db.query(HISMEDDR2).filter(HISMEDDR2.medno == dtlb.fk_medno).all()
            cno = hismedd_data[0].cno if hismedd_data else None

            if cno:
                # 查詢 NHIORDBR2
                ordb_data = db.query(NHIORDBR2).filter(NHIORDBR2.accession_number == dtlb.accession_number).all()

                for ordb in ordb_data:
                    # 創建 R2 類實例
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

        # 提交資料變更
        # for dtlb in dtlb_data:
        #     dtlb.is_analyzed = True  # 標記為已分析

        if merged_data:
            db.add_all(merged_data)
            db.commit()

        return {"message": "Data merged successfully"}

    except Exception as e:
        system_logger.error(exception_message(e))
        db.rollback()  # 確保在出錯時回滾
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