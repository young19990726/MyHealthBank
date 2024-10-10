from datetime import date, datetime
from pydantic import BaseModel, Field


class NHIDTLBR2Base(BaseModel):

    '''住院資料 -> SYBASE ASE -> SybaseIPDHistory(HISHISTORY) -> NHIDTLB'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    fk_medno: str | None = Field(None, description="Medical number")
    accession_number: str | None = Field(None, description="Accession number")
    admission_date: date | None = Field(None, description="Admission date")
    discharge_date: date | None = Field(None, description="Discharge date")
    cm_code: str | None = Field(None, description="ICD clinical modification code")
    pcs_code: str | None = Field(None, description="ICD procedure coding system code")
    is_analyzed: bool | None = Field(None, description="Is analyzed?")
    create_time: datetime | None = Field(None, description="Create time of this data")

    class Config:
      
        from_attributes = True