from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from app.core.settings import settings


@dataclass
class GenResult:
    provider: str
    text: str
    tokens_est: int


class AIProvider(Protocol):
    name: str

    def generate(self, system: str, user_prompt: str) -> GenResult: ...


class StubProvider:
    name = "stub"

    def generate(self, system: str, user_prompt: str) -> GenResult:
        tokens_est = max(1, (len(system) + len(user_prompt)) // 4)
        text = (
            "Vibe Coding means using rapid AI-assisted iteration to prototype, "
            "refactor, and ship features with tight feedback loops."
        )
        return GenResult(provider=self.name, text=text, tokens_est=tokens_est)


class OpenAIProvider:
    name = "openai"

    def __init__(self) -> None:
        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")

        # Official OpenAI SDK client
        from openai import OpenAI  # imported lazily to avoid import cost when using stub

        self._client = OpenAI(api_key=settings.openai_api_key)

    def generate(self, system: str, user_prompt: str) -> GenResult:
        # Use Responses API (recommended for new projects)
        # https://platform.openai.com/docs/guides/text
        resp = self._client.responses.create(
            model=settings.openai_model,
            input=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt},
            ],
            # A conservative ceiling; tune later
            max_output_tokens=256,
            # Many SDKs accept timeout at client-level; keep code minimal here.
        )

        # The SDK provides a convenience field for text output in many examples
        text = getattr(resp, "output_text", None)
        if not text:
            # Fallback: be defensive if SDK response shape changes
            text = str(resp)

        # Tokens: usage fields can vary; use a safe estimate if not present
        tokens_est = 0
        usage = getattr(resp, "usage", None)
        if usage:
            tokens_est = int(getattr(usage, "total_tokens", 0) or 0)
        if tokens_est <= 0:
            tokens_est = max(1, (len(system) + len(user_prompt) + len(text)) // 4)

        return GenResult(provider=self.name, text=text, tokens_est=tokens_est)


def get_provider() -> AIProvider:
    if settings.ai_provider.lower() == "openai":
        return OpenAIProvider()
    return StubProvider()
