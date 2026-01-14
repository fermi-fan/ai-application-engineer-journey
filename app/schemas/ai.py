from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=5000, description="The prompt to send to the AI model.")

class ChatResponse(BaseModel):
    request_id: str
    provider: str
    latency_ms: int
    tokens_est: int
    answer: str

class ExplainRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=200, description="The topic to explain.")
    context: str = Field(..., max_length=5000, description="Additional context for the explanation.")

class ExplainResponse(BaseModel):
    explanation_id: str
    provider: str
    latency_ms: int
    tokens_est: int
    summary: str
    risks: str
    next_steps: str