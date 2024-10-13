from datetime import date, datetime
from pydantic import BaseModel, Field


class FxyreportR8Base(BaseModel):

    '''影像或病理檢驗(查)報告資料 -> SQL SERVER -> RPTDATA -> FXYREPORT'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    cno: str | None = Field(None, description="CNO")
    performed_start_date: date | None = Field(None, description="Performed start date")
    fk_hos_ordercode: str | None = Field(None, description="Internal hospital order code")
    report_text: str | None = Field(None, description="Report text")
    is_analyzed: bool | None = Field(None, description="Is analyzed?")
    create_time: datetime | None = Field(None, description="Create time of this data")

    class Config:
      
        from_attributes = True