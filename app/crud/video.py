from sqlalchemy.orm import Session
from app.db.models.video import Video
from app.schemas.video import VideoCreate

def create_video(db: Session, video: VideoCreate) -> Video:
    db_video = Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_videos(db: Session) -> list[Video]:
    return db.query(Video).all()
