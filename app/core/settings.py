from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    ai_provider: str = os.getenv("AI_PROVIDER", "stub")  # stub | openai
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    openai_timeout_s: float = float(os.getenv("OPENAI_TIMEOUT_S", "30"))


settings = Settings()
