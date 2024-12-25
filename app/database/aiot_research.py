from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker

from app.configs.config import dbSettings


SQLALCHEMY_DATABASE_URL = URL.create(
  f"mssql+pymssql",
    username=dbSettings.AIOT_USER,
    password=dbSettings.AIOT_PASSWORD,
    host=dbSettings.AIOT_HOSTNAME,
    port=dbSettings.AIOT_PORT,
    database=dbSettings.AIOT_NAME
)

Engine_AIOT = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"client_encoding": "utf8"} # Set the database encoding to UTF-8
)

Session_AIOT = sessionmaker(
    autocommit=False, # Disable autocommit so that transaction commits can be managed manually
    autoflush=False,  # Disable auto-refresh to avoid automatically refreshing the session before executing the query
    bind=Engine_AIOT  # Bind the session to the database engine created earlier
)

def get_conn_aiot():
    
    db = Session_AIOT()
    
    try:
        yield db
    
    except Exception:
        db.rollback()
        raise
    
    finally:
        db.close()