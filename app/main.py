from fastapi import FastAPI
import app.models.test as test_schema
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=["*"],
    allow_methods=["*"],
)

test_schema.Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health():
    return {"status": "ok"}