from datetime import date, datetime
from pydantic import BaseModel, Field


class ORDFAR1Base(BaseModel):

    '''西醫門診資料 -> ORACLE -> HIS_2_history(HIS2USERS) -> ORDFA + ORDFA_OLD'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    fk_dtlid: str | None = Field(None, description="DTLFA UUID")
    order_code: str | None = Field(None, description="Physician order code")
    total_number: str | None = Field(None, description="Total number of medical orders")
    dose_day: str | None = Field(None, description="Dosing days")
    is_analyzed: bool | None = Field(None, description="Is analyzed?")
    create_time: datetime | None = Field(None, description="Create time of this data")

    class Config:
      
        from_attributes = True