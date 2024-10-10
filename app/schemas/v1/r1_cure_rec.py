from datetime import date, datetime
from pydantic import BaseModel, Field


class CureRecR1Base(BaseModel):

    '''西醫門診資料 -> ORACLE -> HIS_2_history(HIS2USERS) -> CURE_REC'''

    uid: int | None = Field(None, description="ID")
    hos: str | None = Field(None, description="Hospital ID")
    accession_number: str | None = Field(None, description="Accession number")
    fk_hos_ordercode: str | None = Field(None, description="Internal hospital order code")

    class Config:
      
        from_attributes = True