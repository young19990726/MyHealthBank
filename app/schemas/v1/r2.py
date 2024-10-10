from datetime import date, datetime
from pydantic import BaseModel, Field


class R2Base(BaseModel):

    '''住院資料 -> SYBASE ASE -> SybaseIPDHistory(HISHISTORY) -> NHIORDB'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    cno: str | None = Field(None, description="CNO")
    fk_medno: str | None = Field(None, description="Medical number")
    execution_date: date | None = Field(None, description="Execution date of medical orders")
    expiration_date: date | None = Field(None, description="Expiration date of medical orders")
    order_code: str | None = Field(None, description="Physician order code")
    total_number: str | None = Field(None, description="Total number of medical orders")
    create_time: datetime | None = Field(None, description="Create time of this data")
    admission_date: date | None = Field(None, description="Admission date")
    discharge_date: date | None = Field(None, description="Discharge date")
    cm_code: str | None = Field(None, description="ICD clinical modification code")
    pcs_code: str | None = Field(None, description="ICD procedure coding system code")
    accession_number: str | None = Field(None, description="Accession number")

    class Config:
      
        from_attributes = True