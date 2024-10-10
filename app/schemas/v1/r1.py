from datetime import date, datetime
from pydantic import BaseModel, Field


class R1Base(BaseModel):

    '''西醫門診資料 -> ORACLE -> HIS_2_history(HIS2USERS) -> ORDFA + ORDFA_OLD'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    dtlid: str | None = Field(None, description="DTLFA UUID")
    cno: str | None = Field(None, description="CNO")
    treatment_date: date | None = Field(None, description="Treatment date")
    cm_code: str | None = Field(None, description="ICD clinical modification code")
    pcs_code: str | None = Field(None, description="ICD procedure coding system code")
    order_code: str | None = Field(None, description="Physician order code")
    total_number: str | None = Field(None, description="Total number of medical orders")
    dose_day: str | None = Field(None, description="Dosing days")
    create_time: datetime | None = Field(None, description="Create time of this data")
    
    class Config:
      
        from_attributes = True