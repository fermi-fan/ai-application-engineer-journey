from fastapi import FastAPI

from app.api.ai import router as ai_router
from app.api.health import router as health_router

app = FastAPI(title="AI Application Engineer Journey")

app.include_router(health_router)
app.include_router(ai_router)


@app.get("/")
def root():
    return {"message": "AI Application Engineer Journey started"}
