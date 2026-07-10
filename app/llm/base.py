from typing import Protocol, TypeVar

from pydantic import BaseModel, Field

SchemaT = TypeVar("SchemaT", bound=BaseModel)


class LLMUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class LLMResponse(BaseModel):
    content: str
    usage: LLMUsage = Field(default_factory=LLMUsage)
    model: str
    provider: str


class LLMProvider(Protocol):
    provider_name: str

    def generate(self, prompt: str, *, trace_id: str | None = None) -> LLMResponse:
        raise NotImplementedError

    def generate_structured(
        self,
        prompt: str,
        schema: type[SchemaT],
        *,
        trace_id: str | None = None,
    ) -> SchemaT:
        raise NotImplementedError
