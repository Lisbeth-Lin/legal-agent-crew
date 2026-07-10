import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError

from app.core.exceptions import ConfigError


class SourcesConfig(BaseModel):
    trusted_domains: list[str] = Field(default_factory=list)
    source_priority: dict[str, int] = Field(default_factory=dict)
    blocked_domains: list[str] = Field(default_factory=list)
    institution_mapping: dict[str, str] = Field(default_factory=dict)


class LLMConfig(BaseModel):
    provider: str
    model: str
    base_url: str
    temperature: float = Field(ge=0.0, le=2.0)
    max_tokens: int = Field(gt=0)
    api_key: str | None = None


class EmbeddingConfig(BaseModel):
    model: str
    vector_dim: int = Field(gt=0)


class RerankerConfig(BaseModel):
    model: str


class ModelsConfig(BaseModel):
    llm: LLMConfig
    embedding: EmbeddingConfig
    reranker: RerankerConfig


class RetrievalConfig(BaseModel):
    bm25_top_k: int = Field(gt=0)
    dense_top_k: int = Field(gt=0)
    rerank_top_k: int = Field(gt=0)
    rrf_k: int = Field(gt=0)
    score_threshold: float = Field(ge=0.0)
    metadata_filters: dict[str, str | None] = Field(default_factory=dict)


class PromptConfig(BaseModel):
    version: str
    template: str


class PromptsConfig(BaseModel):
    query_classifier: PromptConfig
    query_rewrite: PromptConfig
    answerability: PromptConfig
    legal_reasoning: PromptConfig
    citation_verifier: PromptConfig


class EvaluationConfig(BaseModel):
    ragas: dict[str, object] = Field(default_factory=dict)
    custom_metrics: dict[str, bool] = Field(default_factory=dict)


class DatabaseConfig(BaseModel):
    database_url: str
    pool_pre_ping: bool = True
    echo_sql: bool = False
    milvus_uri: str
    elasticsearch_url: str


class SecurityConfig(BaseModel):
    max_pdf_size_mb: int = Field(gt=0)
    allowed_extensions: list[str]
    allowed_mime_types: list[str]
    cors_origins: list[str] = Field(default_factory=list)
    rate_limit_per_minute: int = Field(gt=0)


class RuntimeAppConfig(BaseModel):
    name: str
    environment: str
    api_prefix: str
    log_level: str
    enable_langfuse: bool = False


class AppSettings(BaseModel):
    app: RuntimeAppConfig
    sources: SourcesConfig
    models: ModelsConfig
    retrieval: RetrievalConfig
    prompts: PromptsConfig
    evaluation: EvaluationConfig
    database: DatabaseConfig
    security: SecurityConfig


def _read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Missing config file: {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise ConfigError(f"Config file must contain a mapping: {path}")
    return raw


def _deep_update(base: dict[str, Any], override: Mapping[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(merged.get(key), dict):
            merged[key] = _deep_update(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_settings(
    config_dir: Path | None = None,
    env_file: Path | None = None,
    overrides: Mapping[str, Any] | None = None,
) -> AppSettings:
    root = config_dir or Path("config")
    if env_file is not None:
        load_dotenv(env_file)
    else:
        load_dotenv()

    data: dict[str, Any] = {
        "app": _read_yaml(root / "app.yaml"),
        "sources": _read_yaml(root / "sources.yaml"),
        "models": _read_yaml(root / "models.yaml"),
        "retrieval": _read_yaml(root / "retrieval.yaml"),
        "prompts": _read_yaml(root / "prompts.yaml"),
        "evaluation": _read_yaml(root / "evaluation.yaml"),
        "database": _read_yaml(root / "database.yaml"),
        "security": _read_yaml(root / "security.yaml"),
    }

    data["models"]["llm"]["provider"] = os.getenv("LLM_PROVIDER", data["models"]["llm"]["provider"])
    data["models"]["llm"]["model"] = os.getenv("LLM_MODEL", data["models"]["llm"]["model"])
    data["models"]["llm"]["base_url"] = os.getenv("LLM_BASE_URL", data["models"]["llm"]["base_url"])
    data["models"]["llm"]["api_key"] = os.getenv("LLM_API_KEY") or os.getenv("QWEN_API_KEY")
    data["database"]["database_url"] = os.getenv("DATABASE_URL", data["database"]["database_url"])
    data["database"]["milvus_uri"] = os.getenv("MILVUS_URI", data["database"]["milvus_uri"])
    data["database"]["elasticsearch_url"] = os.getenv(
        "ELASTICSEARCH_URL", data["database"]["elasticsearch_url"]
    )

    if overrides:
        data = _deep_update(data, overrides)

    try:
        return AppSettings.model_validate(data)
    except ValidationError as exc:
        raise ConfigError(str(exc)) from exc


settings = load_settings()
