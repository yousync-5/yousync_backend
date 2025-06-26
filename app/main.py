from fastapi import FastAPI
from app.api.routes import video
from app.api.routes import init


app = FastAPI()
app.include_router(video.router)
app.include_router(init.router)