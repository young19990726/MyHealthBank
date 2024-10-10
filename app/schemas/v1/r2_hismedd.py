from datetime import date, datetime
from pydantic import BaseModel, Field


class HISMEDDR2Base(BaseModel):

    '''住院資料 -> SYBASE ASE -> SybaseIPDHistory(HISHISTORY) -> HISMEDD'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    medno: str | None = Field(None, description="Medical number")
    cno: str | None = Field(None, description="CNO")

    class Config:
      
        from_attributes = True