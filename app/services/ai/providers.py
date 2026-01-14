from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class AIResult:
    provider: str
    text: str
    tokens_est: int


class AIProvider(Protocol):
    name: str

    def generate(self, prompt: str) -> AIResult:
        ...


class StubProvider:
    name = "stub"

    def generate(self, prompt: str) -> AIResult:
        # 简单估算 token：按字符粗略换算（后续接真实模型可替换为真实 usage）
        tokens_est = max(1, len(prompt) // 4)
        text = "[stub] Vibe Coding means using rapid AI-assisted iteration to prototype, refactor, and ship features with tight feedback loops."
        return AIResult(provider=self.name, text=text, tokens_est=tokens_est)
