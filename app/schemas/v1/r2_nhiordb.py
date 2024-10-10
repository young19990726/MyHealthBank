from datetime import date, datetime
from pydantic import BaseModel, Field


class NHIORDBR2Base(BaseModel):

    '''住院資料 -> SYBASE ASE -> SybaseIPDHistory(HISHISTORY) -> NHIORDB'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    fk_medno: str | None = Field(None, description="Medical number")
    accession_number: str | None = Field(None, description="Accession number")
    execution_date: date | None = Field(None, description="Execution date of medical orders")
    expiration_date: date | None = Field(None, description="Expiration date of medical orders")
    order_code: str | None = Field(None, description="Physician order code")
    total_number: str | None = Field(None, description="Total number of medical orders")
    is_analyzed: bool | None = Field(None, description="Is analyzed?")
    create_time: datetime | None = Field(None, description="Create time of this data")

    class Config:
      
        from_attributes = True