from dataclasses import dataclass

@dataclass(frozen=True)
class PromptTemplate:
    name: str
    template: str

CHAT_V1 = PromptTemplate(
    name="chat_v1",
    template=(
        "You are a helpful assistant.\n"
        "User prompt:\n"
        "{prompt}\n"
        "Return a concise answer."
    ),
)

EXPLAIN_V1 = PromptTemplate(
    name="explain_v1",
    template=(
        "You are an AI application engineer.\n"
        "Task: Explain the topic clearly for a developer.\n"
        "Topic: {topic}\n"
        "Context: {context}\n"
        "Return JSON with keys: summary, risks, next_steps.\n"
        "Constraints:\n"
        "- summary: string\n"
        "- risks: array of strings (<=5)\n"
        "- next_steps: array of strings (<=5)\n"
    ),
)


def render(template: PromptTemplate, **params: str) -> str:
    return template.template.format(**params)    