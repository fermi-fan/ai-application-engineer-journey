from __future__ import annotations

import time
import uuid
import logging

from app.services.ai.providers import get_provider

logger = logging.getLogger("ai")


def chat(prompt: str) -> dict:
    request_id = uuid.uuid4().hex
    t0 = time.perf_counter()

    provider = get_provider()
    system = "You are a helpful assistant."
    result = provider.generate(system=system, user_prompt=prompt)

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

    provider = get_provider()
    system = "You are a senior software engineer. Explain clearly and concisely."
    user_prompt = f"Topic: {topic}\nContext: {context or ''}".strip()
    result = provider.generate(system=system, user_prompt=user_prompt)

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
            "Add retries/timeouts and basic rate limiting.",
            "Add response caching for repeated prompts.",
            "Add eval tests for regressions (golden prompts).",
        ],
    }
