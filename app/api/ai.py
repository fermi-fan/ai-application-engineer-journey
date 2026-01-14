from fastapi import APIRouter
from app.schemas.ai import ChatRequest, ChatResponse, ExplainRequest, ExplainResponse
from app.services.ai import service as ai_service

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    return ChatResponse(**ai_service.chat(req.prompt))

@router.post("/explain", response_model=ExplainResponse)
def explain(req: ExplainRequest) -> ExplainResponse:
    return ExplainResponse(**ai_service.explain(req.topic, req.context))
