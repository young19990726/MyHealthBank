from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

from app.configs.config import dbSettings

SQLALCHEMY_DATABASE_URL = URL.create(
  f"postgresql",
    username=dbSettings.DB_USER,
    password=dbSettings.DB_PASSWORD,
    host=dbSettings.DB_HOSTNAME,
    port=dbSettings.DB_PORT,
    database=dbSettings.DB_NAME
)

Engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

def get_conn():

    db = Session()
    
    try:
        yield db
    
    except Exception:
        db.rollback()
        raise
    
    finally:
        db.close()