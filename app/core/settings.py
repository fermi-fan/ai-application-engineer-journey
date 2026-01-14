from pydantic import BaseModel

class Settings(BaseModel):
    ai_provider: str = "stub" # stub | openai | claude | local

settings = Settings()
    