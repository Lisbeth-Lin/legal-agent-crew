from pathlib import Path

import pytest

from app.core.config import load_settings
from app.core.exceptions import ConfigError


@pytest.mark.unit
def test_missing_config_file_raises_config_error(tmp_path: Path) -> None:
    with pytest.raises(ConfigError):
        load_settings(config_dir=tmp_path)


@pytest.mark.unit
def test_settings_override_retrieval_config() -> None:
    settings = load_settings(overrides={"retrieval": {"dense_top_k": 7}})

    assert settings.retrieval.dense_top_k == 7
    assert settings.retrieval.bm25_top_k == 20


@pytest.mark.unit
def test_environment_overrides_database_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./data/test-override.db")

    settings = load_settings()

    assert settings.database.database_url == "sqlite:///./data/test-override.db"
