from pydantic import BaseModel

from app.llm.base import LLMProvider, LLMResponse, LLMUsage, SchemaT


class FakeLLMProvider(LLMProvider):
    provider_name = "fake"

    def __init__(self, response_text: str = "FAKE_RESPONSE") -> None:
        self.response_text = response_text

    def generate(self, prompt: str, *, trace_id: str | None = None) -> LLMResponse:
        return LLMResponse(
            content=self.response_text,
            usage=LLMUsage(
                prompt_tokens=len(prompt.split()),
                completion_tokens=len(self.response_text.split()),
                total_tokens=len(prompt.split()) + len(self.response_text.split()),
            ),
            model="fake-model",
            provider=self.provider_name,
        )

    def generate_structured(
        self,
        prompt: str,
        schema: type[SchemaT],
        *,
        trace_id: str | None = None,
    ) -> SchemaT:
        if not issubclass(schema, BaseModel):
            raise TypeError("schema must be a Pydantic model")
        return schema.model_validate_json(self.response_text)
