from pydantic import BaseModel

class VideoBase(BaseModel):
    actor: str
    total_time: int
    category: str
    url: str
    bookmark: bool = False

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True
