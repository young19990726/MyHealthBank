import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Settings():
    VERSION: str = "beta24.10"
    SERVICE_DEBUG: bool = os.getenv('SERVICE_DEBUG', False) == 'True'
    SERVICE_PORT = int(os.getenv('FASTAPI_PORT'))
    WORKER_COUNT = int(os.getenv('WORKER_COUNT'))
    # BASE_PATH: str = "https://ailab.ndmctsgh.edu.tw/aiot_devteam/s/312fc3c9ab5a788483945/p/4e5a6864/" 
    BASE_PATH: str = "https://ailab.ndmctsgh.edu.tw/aiot_devteam/s/312fc3c9ab5a7fa517810/p/9caaeb9d/"
    BASE_PREFIX: str = "/api/v1"

basicSettings = Settings()

class DatabaseSettings(BaseSettings):
    SERVICE_DEBUG: bool
    FASTAPI_PORT: str
    WORKER_COUNT: int

    DB_USER: str
    DB_PASSWORD: str
    DB_HOSTNAME: str
    DB_PORT: str
    DB_NAME: str

    AIOT_USER: str
    AIOT_PASSWORD: str
    AIOT_HOSTNAME: str
    AIOT_PORT: str
    AIOT_NAME: str
    
    class Config:
        env_file = 'app/.env'

dbSettings = DatabaseSettings()

