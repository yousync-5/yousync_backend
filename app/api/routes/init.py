from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.video import Video

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/init-dummy-videos")
def init_dummy_videos(db: Session = Depends(get_db)):
    dummy_data = [
        Video(actor="Natalie Portman", total_time=34, category="여자 배우", url="https://youtu.be/_Q27uim6ZN4", bookmark=False),
        Video(actor="Tom Hanks", total_time=120, category="남자 배우", url="https://youtu.be/lT4jmjkagao", bookmark=False),
        Video(actor="Emma Stone", total_time=45, category="여자 배우", url="https://youtu.be/b65C_muXajk", bookmark=False),
        Video(actor="Christian Bale", total_time=45, category="남자 배우", url="https://youtu.be/VdG34y8kUyc", bookmark=False),
        Video(actor="Liam Neeson", total_time=45, category="남자 배우", url="https://youtu.be/jZOywn1qArI", bookmark=False),
        Video(actor="Rachel McAdams", total_time=45, category="여자 배우", url="https://youtu.be/8tNiR96vkW0", bookmark=False)
    ]
    db.add_all(dummy_data)
    db.commit()
    return {"message": f"{len(dummy_data)}개의 더미 영상이 추가되었습니다."}
