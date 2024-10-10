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
# @router.post("", response_model=R7Base, name="Post r7", description="Post r7", include_in_schema=True)
# async def post_r7(
#     db: Session = Depends(get_conn)
# ):
#     try:
#         fexreport_data = db.query(FexreportR7).filter(FexreportR7.is_analyzed == False).all()
#         merged_data = []

#         for fexreport in fexreport_data:

#             if fexreport.order_code == 'None':
#                 accession_number = fexreport.fk_accession_number

#                 # 用來存放該 accession_number 找到的所有 order_code
#                 order_codes = []

#                 # 查詢所有與該 accession_number 關聯的 CureRecR1 資料
#                 cure_rec_data = db.query(CureRecR1).filter(CureRecR1.accession_number == accession_number).all()

#                 for cure_rec in cure_rec_data:
#                     fk_hos_ordercode = cure_rec.fk_hos_ordercode
#                     # 查詢 OrderCodeMasterR1 資料
#                     order_code_master_data = db.query(OrderCodeMasterR1).filter(OrderCodeMasterR1.hos_ordercode == fk_hos_ordercode).first()

#                     if order_code_master_data and order_code_master_data.order_code not in order_codes:
#                         # 如果找到了對應的 order_code，將其加入列表
#                         order_codes.append(order_code_master_data.order_code)
#                 print(order_codes)
#                 # 如果有找到 order_code，將其轉換為逗號分隔的字串
#                 if order_codes:
#                     fexreport.order_code = ",".join(order_codes)
#                 else:
#                     system_logger.warning(f"No order_code found for accession_number: {accession_number}")
#                     continue  # 如果沒有找到任何 order_code，跳過當前循環

#             # 將處理後的資料轉換為 R7 model
#             model = R7(
#                 hos=fexreport.hos,
#                 cno=fexreport.cno,
#                 report_date=fexreport.report_date,
#                 fk_accession_number=fexreport.fk_accession_number,
#                 ordclnm_name=fexreport.ordclnm_name,
#                 data=fexreport.data,
#                 order_code=fexreport.order_code,
#             )
#             merged_data.append(model)
#         print(merged_data)
#         if merged_data:
#             db.add_all(merged_data)
#             db.commit()

#             # 標記所有 fexreport 為已分析
#             for fexreport in fexreport_data:
#                 fexreport.is_analyzed = True
#             db.commit()

#         return {"detail": "Data merged and stored successfully."}

#     except IntegrityError as e:
#         system_logger.error(exception_message(e))
#         raise HTTPException(status_code=400, detail="Integrity error with the provided data")

#     except Exception as e:
#         db.rollback()
#         system_logger.error(exception_message(e))
#         raise HTTPException(status_code=500, detail="Error post r7")
@router.post("", response_model=R7Base, name="Post r7", description="Post r7", include_in_schema=True)
async def post_r7(
    db: Session = Depends(get_conn)
):
    try:
        fexreport_data = db.query(FexreportR7).filter(FexreportR7.is_analyzed == False).all()
        merged_data = []

        for fexreport in fexreport_data:

            accession_number = fexreport.fk_accession_number

                # 用來存放該 accession_number 找到的所有 order_code
            order_codes = []

                # 查詢所有與該 accession_number 關聯的 CureRecR1 資料
            cure_rec_data = db.query(CureRecR1).filter(CureRecR1.accession_number == accession_number).all()

            for cure_rec in cure_rec_data:
                fk_hos_ordercode = cure_rec.fk_hos_ordercode
                    # 查詢 OrderCodeMasterR1 資料
                order_code_master_data = db.query(OrderCodeMasterR1).filter(OrderCodeMasterR1.hos_ordercode == fk_hos_ordercode).first()

                if order_code_master_data and order_code_master_data.order_code not in order_codes:
                        # 如果找到了對應的 order_code，將其加入列表
                    order_codes.append(order_code_master_data.order_code)

                # 如果有找到 order_code，將其轉換為逗號分隔的字串
            
            fexreport_order_code = ",".join(order_codes)

                    # 將處理後的資料轉換為 R7 model
            model = R7(
                hos=fexreport.hos,
                cno=fexreport.cno,
                report_date=fexreport.report_date,
                fk_accession_number=fexreport.fk_accession_number,
                ordclnm_name=fexreport.ordclnm_name,
                data=fexreport.data,
                order_code=fexreport_order_code,  # 使用新的 order_code
            )
            merged_data.append(model)

            # else:
            #     system_logger.warning(f"No order_code found for accession_number: {accession_number}")
            #     continue  # 如果沒有找到任何 order_code，跳過當前循環
            
            # 判斷 fexreport.order_code 是否為 'None'
            # if fexreport.order_code == 'None':
            # if fexreport.order_code is not None:
            #     accession_number = fexreport.fk_accession_number

            #     # 用來存放該 accession_number 找到的所有 order_code
            #     order_codes = []

            #     # 查詢所有與該 accession_number 關聯的 CureRecR1 資料
            #     cure_rec_data = db.query(CureRecR1).filter(CureRecR1.accession_number == accession_number).all()

            #     for cure_rec in cure_rec_data:
            #         fk_hos_ordercode = cure_rec.fk_hos_ordercode
            #         # 查詢 OrderCodeMasterR1 資料
            #         order_code_master_data = db.query(OrderCodeMasterR1).filter(OrderCodeMasterR1.hos_ordercode == fk_hos_ordercode).first()

            #         if order_code_master_data and order_code_master_data.order_code not in order_codes:
            #             # 如果找到了對應的 order_code，將其加入列表
            #             order_codes.append(order_code_master_data.order_code)

            #     # 如果有找到 order_code，將其轉換為逗號分隔的字串
            #     if order_codes:
            #         fexreport_order_code = ",".join(order_codes)

            #         # 將處理後的資料轉換為 R7 model
            #         model = R7(
            #             hos=fexreport.hos,
            #             cno=fexreport.cno,
            #             report_date=fexreport.report_date,
            #             fk_accession_number=fexreport.fk_accession_number,
            #             ordclnm_name=fexreport.ordclnm_name,
            #             data=fexreport.data,
            #             order_code=fexreport_order_code,  # 使用新的 order_code
            #         )
            #         merged_data.append(model)

            #     else:
            #         system_logger.warning(f"No order_code found for accession_number: {accession_number}")
            #         continue  # 如果沒有找到任何 order_code，跳過當前循環

            # else:
            #     # fexreport.order_code 不是 'None'，直接使用原始的 order_code
            #     model = R7(
            #         hos=fexreport.hos,
            #         cno=fexreport.cno,
            #         report_date=fexreport.report_date,
            #         fk_accession_number=fexreport.fk_accession_number,
            #         ordclnm_name=fexreport.ordclnm_name,
            #         data=fexreport.data,
            #         order_code=fexreport.order_code,  # 使用原始的 order_code
            #     )
            #     merged_data.append(model)

        if merged_data:
            db.add_all(merged_data)  
            for fexreport in fexreport_data:
                fexreport.is_analyzed = True  # 更新分析狀態
            db.commit() 

        return {"detail": "Data merged and stored successfully."}  

    except IntegrityError as e:
        system_logger.error(exception_message(e))  
        raise HTTPException(status_code=400, detail="Integrity error with the provided data") 

    except Exception as e:
        db.rollback()  
        system_logger.error(exception_message(e)) 
        raise HTTPException(status_code=500, detail="Error post r7")

# @router.post("", response_model=R7Base, name="Post r7", description="Post r7", include_in_schema=True)
# async def post_r7(
#     db: Session = Depends(get_conn)
# ):
#     try:
#         fexreport_data = db.query(FexreportR7).filter(FexreportR7.is_analyzed == False).all()
#         merged_data = []

#         for fexreport in fexreport_data:

#             if fexreport.order_code == 'None':
#                 accession_number = fexreport.fk_accession_number

#                 # 用來存放該 accession_number 找到的所有 order_code
#                 order_codes = []

#                 # 查詢所有與該 accession_number 關聯的 CureRecR1 資料
#                 cure_rec_data = db.query(CureRecR1).filter(CureRecR1.accession_number == accession_number).all()

#                 for cure_rec in cure_rec_data:
#                     fk_hos_ordercode = cure_rec.fk_hos_ordercode
#                     # 查詢 OrderCodeMasterR1 資料
#                     order_code_master_data = db.query(OrderCodeMasterR1).filter(OrderCodeMasterR1.hos_ordercode == fk_hos_ordercode).first()

#                     if order_code_master_data and order_code_master_data.order_code not in order_codes:
#                         # 如果找到了對應的 order_code，將其加入列表
#                         order_codes.append(order_code_master_data.order_code)
#                 print(order_codes)
#                 # 如果有找到 order_code，將其轉換為逗號分隔的字串
#                 if order_codes:
#                     fexreport_order_code = ",".join(order_codes)

#                     # 將處理後的資料轉換為 R7 model
#                     model = R7(
#                         hos=fexreport.hos,
#                         cno=fexreport.cno,
#                         report_date=fexreport.report_date,
#                         fk_accession_number=fexreport.fk_accession_number,
#                         ordclnm_name=fexreport.ordclnm_name,
#                         data=fexreport.data,
#                         order_code=fexreport_order_code,
#                     )
#                     merged_data.append(model)

#                 else:
#                     system_logger.warning(f"No order_code found for accession_number: {accession_number}")
#                     continue  # 如果沒有找到任何 order_code，跳過當前循環



#         if merged_data:
#             db.add_all(merged_data)  
#             for fexreport in fexreport_data:
#                 fexreport.is_analyzed = True
#             db.commit() 

#         return {"detail": "Data merged and stored successfully."}  

#     except IntegrityError as e:
#         system_logger.error(exception_message(e))  
#         raise HTTPException(status_code=400, detail="Integrity error with the provided data") 

#     except Exception as e:
#         db.rollback()  
#         system_logger.error(exception_message(e)) 
#         raise HTTPException(status_code=500, detail="Error post r7")

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