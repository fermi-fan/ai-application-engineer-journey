from __future__ import annotations

import json
import time
import uuid
from typing import Any, Dict

from app.core.settings import settings
from app.services.ai.prompts import CHAT_V1, EXPLAIN_V1, render
from app.services.ai.providers import AIProvider, StubProvider


def _get_provider() -> AIProvider:
    # 后续可以按 settings.ai_provider 选择不同 provider
    if settings.ai_provider == "stub":
        return StubProvider()
    # 默认兜底
    return StubProvider()


def chat(prompt: str) -> Dict[str, Any]:
    request_id = uuid.uuid4().hex
    provider = _get_provider()

    t0 = time.perf_counter()
    full_prompt = render(CHAT_V1, prompt=prompt)
    result = provider.generate(full_prompt)
    latency_ms = int((time.perf_counter() - t0) * 1000)

    return {
        "request_id": request_id,
        "provider": result.provider,
        "latency_ms": latency_ms,
        "tokens_est": result.tokens_est,
        "answer": result.text,
    }


def explain(topic: str, context: str) -> Dict[str, Any]:
    request_id = uuid.uuid4().hex
    provider = _get_provider()

    t0 = time.perf_counter()
    full_prompt = render(EXPLAIN_V1, topic=topic, context=context)
    result = provider.generate(full_prompt)
    latency_ms = int((time.perf_counter() - t0) * 1000)

    # stub 返回的不是 JSON，这里做一个“工程兜底”
    parsed: Dict[str, Any]
    try:
        parsed = json.loads(result.text)
    except Exception:
        parsed = {
            "summary": f"Explanation for: {topic}",
            "risks": ["Model output may be inconsistent", "Context may be insufficient"],
            "next_steps": ["Add real provider", "Add eval & logging", "Add retries/timeouts"],
        }

    return {
        "request_id": request_id,
        "provider": result.provider,
        "latency_ms": latency_ms,
        "tokens_est": result.tokens_est,
        "summary": str(parsed.get("summary", "")),
        "risks": list(parsed.get("risks", []))[:5],
        "next_steps": list(parsed.get("next_steps", []))[:5],
    }
