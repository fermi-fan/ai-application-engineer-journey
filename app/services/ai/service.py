from __future__ import annotations

import time
import uuid
from dataclasses import dataclass
import logging

logger = logging.getLogger("ai")

@dataclass
class GenResult:
    provider: str
    text: str
    tokens_est: int


class StubProvider:
    name = "stub"

    def generate(self, system: str, user_prompt: str) -> GenResult:
        # 简单估算 token：按字符/4 粗略估算
        tokens_est = max(1, (len(system) + len(user_prompt)) // 4)
        text = (
            "[stub] Vibe Coding means using rapid AI-assisted iteration to prototype, "
            "refactor, and ship features with tight feedback loops."
        )
        return GenResult(provider=self.name, text=text, tokens_est=tokens_est)


_provider = StubProvider()


def chat(prompt: str) -> dict:
    request_id = uuid.uuid4().hex
    t0 = time.perf_counter()

    system = "You are a helpful assistant."
    result = _provider.generate(system=system, user_prompt=prompt)

    latency_ms = int((time.perf_counter() - t0) * 1000)

    logger.info(
    "ai.chat",
    extra={"extra": {
        "request_id": request_id,
        "provider": result.provider,
        "latency_ms": latency_ms,
        "tokens_est": result.tokens_est,
    }},
)

    return {
        "request_id": request_id,
        "provider": result.provider,
        "latency_ms": latency_ms,
        "tokens_est": result.tokens_est,
        "answer": result.text,
    }


def explain(topic: str, context: str | None = None) -> dict:
    request_id = uuid.uuid4().hex
    t0 = time.perf_counter()

    system = "You are a senior software engineer. Explain clearly and concisely."
    user_prompt = f"Topic: {topic}\nContext: {context or ''}".strip()
    result = _provider.generate(system=system, user_prompt=user_prompt)

    latency_ms = int((time.perf_counter() - t0) * 1000)

    logger.info(
    "ai.explain",
    extra={"extra": {
        "request_id": request_id,
        "provider": result.provider,
        "latency_ms": latency_ms,
        "tokens_est": result.tokens_est,
    }},
)

    return {
        "request_id": request_id,
        "provider": result.provider,
        "latency_ms": latency_ms,
        "tokens_est": result.tokens_est,
        "explanation": result.text,
        "risks": [
            "Model output may be inaccurate or incomplete.",
            "Provided context may be insufficient for the intended task.",
        ],
        "next_steps": [
            "Add a real provider (OpenAI/Claude) behind the same interface.",
            "Add structured logging with request_id and latency.",
            "Add retries/timeouts and basic rate limiting.",
        ],
    }
