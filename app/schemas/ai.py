from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1)


class ChatResponse(BaseModel):
    request_id: str
    provider: str
    latency_ms: int
    tokens_est: int
    answer: str


class ExplainRequest(BaseModel):
    topic: str = Field(min_length=1)
    context: Optional[str] = None


class ExplainResponse(BaseModel):
    request_id: str
    provider: str
    latency_ms: int
    tokens_est: int
    explanation: str
    risks: List[str]
    next_steps: List[str]
