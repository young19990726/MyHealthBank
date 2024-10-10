from datetime import date, datetime
from pydantic import BaseModel, Field


class R7Base(BaseModel):

    '''檢驗(查)結果資料 -> SQL SERVER -> RPTDATA -> FEXREPORT'''
    
    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    cno: str | None = Field(None, description="CNO")
    report_date: date | None = Field(None, description="Inspection date")
    fk_accession_number: str | None = Field(None, description="Accession number(lisacces)")
    ordclnm_name: str | None = Field(None, description="Inspection item name")
    data: str | None = Field(None, description="Inspection result")
    order_code: str | None = Field(None, description="Physician order code")
    is_analyzed: bool | None = Field(None, description="Is analyzed?")
    create_time: datetime | None = Field(None, description="Create time of this data")

    class Config:
      
        from_attributes = True