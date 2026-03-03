from fastapi import FastAPI
import app.models.test as test_schema

from app.core.database import engine
app = FastAPI()

test_schema.Base.metadata.create_all(bind=engine)
@app.get("/health")
async def health():
    return {"status": "ok"}