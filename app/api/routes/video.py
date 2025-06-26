from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.video import Video, VideoCreate
from app.crud import video as crud_video

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/videos", response_model=Video)
def create_video_endpoint(video: VideoCreate, db: Session = Depends(get_db)):
    return crud_video.create_video(db, video)

@router.get("/videos", response_model=list[Video])
def read_videos(db: Session = Depends(get_db)):
    return crud_video.get_videos(db)
