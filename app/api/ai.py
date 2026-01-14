from fastapi import APIRouter, Response
from app.schemas.ai import ChatRequest, ChatResponse, ExplainRequest, ExplainResponse
from app.services.ai import service as ai_service

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, response: Response) -> ChatResponse:
    data = ai_service.chat(req.prompt)
    response.headers["X-Request-ID"] = data["request_id"]
    return ChatResponse(**data)

@router.post("/explain", response_model=ExplainResponse)
def explain(req: ExplainRequest) -> ExplainResponse:
    return ExplainResponse(**ai_service.explain(req.topic, req.context))
