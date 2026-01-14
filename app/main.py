from fastapi import FastAPI

from app.core.logging import setup_logging
from app.core.middleware import request_logging_middleware
from app.api.ai import router as ai_router

setup_logging(level="INFO")

app = FastAPI(title="AI Application Engineer Journey")

# middleware
app.middleware("http")(request_logging_middleware)

# routers
app.include_router(ai_router)


@app.get("/")
def root():
    return {"message": "AI Application Engineer Journey started"}
