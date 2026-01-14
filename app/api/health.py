from fastapi import APIRouter
from app.schemas.health import HealthResponse
from app.services.health_service import get_status

router = APIRouter(prefix="/health", tags=["health"])

@router.get("", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status=get_status())
