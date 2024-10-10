from datetime import date, datetime
from pydantic import BaseModel, Field


class DTLFAR1Base(BaseModel):

    '''西醫門診資料 -> ORACLE -> HIS_2_history(HIS2USERS) -> DTLFA + DTLFA_OLD'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    dtlid: str | None = Field(None, description="DTLFA UUID")
    cno: str | None = Field(None, description="CNO")
    treatment_date: date | None = Field(None, description="Treatment date")
    cm_code: str | None = Field(None, description="ICD clinical modification code")
    pcs_code: str | None = Field(None, description="ICD procedure coding system code")
    is_analyzed: bool | None = Field(None, description="Is analyzed?")
    create_time: datetime | None = Field(None, description="Create time of data")

    class Config:
      
        from_attributes = True