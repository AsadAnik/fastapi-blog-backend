# DATABASE CONFIGURATION PART HERE
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/fastapi_blog_db"

settings = Settings()