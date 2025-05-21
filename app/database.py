from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv() # .env 파일에서 환경 변수 로드

# 데이터베이스 URL 
DATABASE_URL = os.getenv("DATABASE_URL")