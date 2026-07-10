import pytest
from pydantic import BaseModel

from app.core.config import load_settings
from app.core.exceptions import ConfigError
from app.llm.fake import FakeLLMProvider
from app.llm.openai_compatible import OpenAICompatibleProvider
from app.llm.prompt_registry import PromptRegistry


class StructuredAnswer(BaseModel):
    answer: str


@pytest.mark.unit
def test_fake_llm_provider_generates_text() -> None:
    provider = FakeLLMProvider("hello world")

    response = provider.generate("Say hello")

    assert response.content == "hello world"
    assert response.provider == "fake"
    assert response.usage.total_tokens > 0


@pytest.mark.unit
def test_fake_llm_provider_generates_structured_output() -> None:
    provider = FakeLLMProvider('{"answer": "ok"}')

    response = provider.generate_structured("Return JSON", StructuredAnswer)

    assert response.answer == "ok"


@pytest.mark.unit
def test_openai_compatible_provider_requires_api_key() -> None:
    settings = load_settings(overrides={"models": {"llm": {"api_key": None}}})

    with pytest.raises(ConfigError):
        OpenAICompatibleProvider(settings.models.llm)


@pytest.mark.unit
def test_prompt_registry_returns_prompt_metadata() -> None:
    settings = load_settings()
    registry = PromptRegistry(settings.prompts)

    record = registry.get("legal_reasoning")

    assert record.version == "v1"
    assert len(record.prompt_hash) == 64
