from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, func, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship
from app.database.healthbank import Engine

Base = declarative_base()


class OrderCodeMasterR1(Base):
    __tablename__ = "r1_order_code_master"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    hos_ordercode = Column(String(20), index=True)
    order_code = Column(String(20), index=True)

    # r1_cure_rec = relationship("CureRecR1", back_populates="r1_order_code_master")
    # r8_fxyreport = relationship("FxyreportR8", back_populates="r1_order_code_master")


class CureRecR1(Base):
    __tablename__ = "r1_cure_rec"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    accession_number = Column(String(20), index=True)
    fk_hos_ordercode = Column(String(20), index=True) 
    # fk_hos_ordercode = Column(String(20), ForeignKey("r1_order_code_master.hos_ordercode"), index=True) 

    # r1_order_code_master = relationship("OrderCodeMasterR1", back_populates="r1_cure_rec")
    # r7_fexreport = relationship("FexreportR7", back_populates="r1_cure_rec")


class DTLFAR1(Base):
    __tablename__ = "r1_dtlfa"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    dtlid = Column(String(40), unique=True, index=True) 
    cno = Column(String(20), index=True)
    treatment_date = Column(Date)
    cm_code = Column(String(20), index=True)
    pcs_code = Column(String(20), index=True)
    is_analyzed = Column(Boolean, default=False)
    create_time = Column(DateTime, default=func.now())

    # r1_ordfa = relationship("ORDFAR1", back_populates="r1_dtlfa")


class ORDFAR1(Base):
    __tablename__ = "r1_ordfa"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    # fk_dtlid = Column(String(40), ForeignKey("r1_dtlfa.dtlid"), index=True) 
    fk_dtlid = Column(String(40), index=True) 
    order_code = Column(String(20), index=True)
    total_number = Column(String(20), index=True)
    dose_day = Column(String(20), index=True)
    is_analyzed = Column(Boolean, default=False)
    create_time = Column(DateTime, default=func.now())

    # r1_dtlfa = relationship("DTLFAR1", back_populates="r1_ordfa")

class R1(Base):
    __tablename__ = "r1"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    dtlid = Column(String(40), index=True) 
    cno = Column(String(20), index=True)
    treatment_date = Column(Date)
    cm_code = Column(String(20), index=True)
    pcs_code = Column(String(20), index=True)
    order_code = Column(String(20), index=True)
    total_number = Column(String(20), index=True)
    dose_day = Column(String(20), index=True)
    create_time = Column(DateTime, default=func.now())

class HISMEDDR2(Base):
    __tablename__ = "r2_hismedd"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    medno = Column(String(20), unique=True, index=True)
    cno = Column(String(20), index=True)

    # r2_nhidtlb = relationship("NHIDTLBR2", back_populates="r2_hismedd")
    # r2_nhiordb = relationship("NHIORDBR2", back_populates="r2_hismedd")


class NHIDTLBR2(Base):
    __tablename__ = "r2_nhidtlb"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    # fk_medno = Column(String(20), ForeignKey("r2_hismedd.medno"), index=True) 
    fk_medno = Column(String(20), index=True) 
    accession_number = Column(String(20), index=True)
    admission_date = Column(Date)
    discharge_date = Column(Date)
    cm_code = Column(String(20), index=True)
    pcs_code = Column(String(20), index=True)
    is_analyzed = Column(Boolean, default=False)
    create_time = Column(DateTime, default=func.now())

    # r2_hismedd = relationship("HISMEDDR2", back_populates="r2_nhidtlb")


class NHIORDBR2(Base):
    __tablename__ = "r2_nhiordb"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    # fk_medno = Column(String(20), ForeignKey("r2_hismedd.medno"), index=True) 
    fk_medno = Column(String(20), index=True) 
    accession_number = Column(String(20), index=True)
    execution_date = Column(Date)
    expiration_date = Column(Date)
    order_code = Column(String(20), index=True)
    total_number = Column(String(20), index=True)
    is_analyzed = Column(Boolean, default=False)
    create_time = Column(DateTime, default=func.now())

    # r2_hismedd = relationship("HISMEDDR2", back_populates="r2_nhiordb")

class R2(Base):
    __tablename__ = "r2"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    cno = Column(String(20), index=True)
    fk_medno = Column(String(20), index=True) 
    admission_date = Column(Date)
    discharge_date = Column(Date)
    cm_code = Column(String(20), index=True)
    pcs_code = Column(String(20), index=True)
    execution_date = Column(Date)
    expiration_date = Column(Date)
    order_code = Column(String(20), index=True)
    total_number = Column(String(20), index=True)
    accession_number = Column(String(20), index=True)
    create_time = Column(DateTime, default=func.now())


class FexreportR7(Base):
    __tablename__ = "r7_fexreport"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    cno = Column(String(20), index=True)
    report_date = Column(Date)
    # fk_accession_number = Column(String(20), ForeignKey("r1_cure_rec.accession_number"), index=True)
    fk_accession_number = Column(String(20), index=True)    
    ordclnm_name = Column(String(40), index=True)
    data = Column(Text) 
    order_code = Column(Text) 
    is_analyzed = Column(Boolean, default=False)
    create_time = Column(DateTime, default=func.now())

    # r1_cure_rec = relationship("CureRecR1", back_populates="r7_fexreport")

class R7(Base):
    __tablename__ = "r7"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    cno = Column(String(20), index=True)
    report_date = Column(Date)
    fk_accession_number = Column(String(20), index=True)    
    ordclnm_name = Column(String(40), index=True)
    data = Column(Text) 
    order_code = Column(Text) 
    create_time = Column(DateTime, default=func.now())


class FxyreportR8(Base):
    __tablename__ = "r8_fxyreport"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    cno = Column(String(20), index=True)
    performed_start_date = Column(Date)
    # fk_hos_ordercode = Column(String(20), ForeignKey("r1_order_code_master.hos_ordercode"), index=True) 
    fk_hos_ordercode = Column(String(20), index=True) 
    # order_code = Column(String(20), index=True)
    report_text = Column(Text)
    is_analyzed = Column(Boolean, default=False)
    create_time = Column(DateTime, default=func.now())

    # r1_order_code_master = relationship("OrderCodeMasterR1", back_populates="r8_fxyreport")


class R8(Base):
    __tablename__ = "r8"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    hos = Column(String(10), index=True)
    cno = Column(String(20), index=True)
    performed_start_date = Column(Date)
    order_code = Column(String(20), index=True) 
    report_text = Column(Text) 
    create_time = Column(DateTime, default=func.now())


Base.metadata.create_all(bind=Engine)
