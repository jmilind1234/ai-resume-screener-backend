from fastapi import FastAPI
import app.models.User as user_model
import app.models.Resume as resume_model
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine
from app.routers import auth
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=["*"],
    allow_methods=["*"],
)

user_model.Base.metadata.create_all(bind=engine)
resume_model.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)