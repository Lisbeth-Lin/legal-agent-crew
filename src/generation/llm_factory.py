import os
from typing import Optional

from crewai import LLM

from config.settings import settings


def get_llm_provider() -> str:
    return (settings.llm_provider or "qwen").strip().lower()


def get_llm_api_key_env_name() -> str:
    provider = get_llm_provider()
    if provider == "qwen":
        return "QWEN_API_KEY"
    if provider == "openai":
        return "OPENAI_API_KEY"
    raise ValueError(f"Unsupported LLM provider: {provider}")


def get_llm_api_key(api_key: Optional[str] = None) -> str:
    provider = get_llm_provider()
    if provider == "qwen":
        return api_key or settings.qwen_api_key or os.getenv("QWEN_API_KEY", "")
    if provider == "openai":
        return api_key or settings.openai_api_key or os.getenv("OPENAI_API_KEY", "")
    raise ValueError(f"Unsupported LLM provider: {provider}")


def get_active_llm_model() -> str:
    provider = get_llm_provider()
    if provider == "qwen":
        return settings.qwen_model
    if provider == "openai":
        return settings.llm_model
    raise ValueError(f"Unsupported LLM provider: {provider}")


def _litellm_openai_compatible_model(model: str) -> str:
    if model.startswith(("openai/", "azure/", "dashscope/")):
        return model
    return f"openai/{model}"


def create_llm(
    model: Optional[str] = None,
    api_key: Optional[str] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
) -> LLM:
    provider = get_llm_provider()
    resolved_api_key = get_llm_api_key(api_key)
    if not resolved_api_key:
        raise ValueError(f"{get_llm_api_key_env_name()} is required for LLM provider '{provider}'.")

    if provider == "qwen":
        resolved_model = _litellm_openai_compatible_model(model or settings.qwen_model)
        return LLM(
            model=resolved_model,
            api_key=resolved_api_key,
            base_url=settings.qwen_base_url,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    if provider == "openai":
        return LLM(
            model=model or settings.llm_model,
            api_key=resolved_api_key,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    raise ValueError(f"Unsupported LLM provider: {provider}")
