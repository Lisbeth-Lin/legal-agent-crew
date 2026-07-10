from app.core.config import LLMConfig
from app.core.exceptions import ConfigError
from app.llm.base import LLMProvider, LLMResponse, SchemaT


class OpenAICompatibleProvider(LLMProvider):
    provider_name = "openai_compatible"

    def __init__(self, config: LLMConfig) -> None:
        if not config.api_key:
            raise ConfigError("LLM API key is required for OpenAI-compatible provider")
        self.config = config

    def generate(self, prompt: str, *, trace_id: str | None = None) -> LLMResponse:
        raise NotImplementedError("Network LLM calls are deferred until generator modules use this")

    def generate_structured(
        self,
        prompt: str,
        schema: type[SchemaT],
        *,
        trace_id: str | None = None,
    ) -> SchemaT:
        response = self.generate(prompt, trace_id=trace_id)
        return schema.model_validate_json(response.content)
