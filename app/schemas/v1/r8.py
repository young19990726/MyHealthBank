from datetime import date, datetime
from pydantic import BaseModel, Field


class R8Base(BaseModel):

    '''影像或病理檢驗(查)報告資料 -> SQL SERVER -> RPTDATA -> FXYREPORT'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    cno: str | None = Field(None, description="CNO")
    performed_start_date: date | None = Field(None, description="Performed start date")
    order_code: str | None = Field(None, description="Physician order code")
    report_text: str | None = Field(None, description="Report text")
    create_time: datetime | None = Field(None, description="Create time of this data")

    class Config:
      
        from_attributes = True