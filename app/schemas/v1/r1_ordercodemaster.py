from datetime import date, datetime
from pydantic import BaseModel, Field


class OrderCodeMasterR1Base(BaseModel):

    '''西醫門診資料 -> ORACLE -> HIS_2_history(HIS2USERS) -> ORDERCODEMASTER'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    hos_ordercode: str | None = Field(None, description="Internal hospital order code")
    order_code: str | None = Field(None, description="Physician order code")

    class Config:
      
        from_attributes = True