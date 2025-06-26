from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
from app.db.base import Base 

# Base = declarative_base()

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    actor = Column(String, nullable=False)
    total_time = Column(Integer, nullable=False)
    category = Column(String, nullable=True)
    url = Column(String, nullable=False)
    bookmark = Column(Boolean, default=False)
