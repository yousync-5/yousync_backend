# app/core/config.py

# .env 파일을 FastAPI 앱에서 불러오기 위한 설정 파일
from pydantic_settings import BaseSettings  # ✅ 수정된 import 경로

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
