import tomllib
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.unit
def test_pyproject_declares_current_project() -> None:
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["name"] == "paralegal-agent"
    assert pyproject["project"]["requires-python"] == ">=3.13,<3.14"


@pytest.mark.unit
def test_legacy_streamlit_prototype_entrypoint_is_preserved() -> None:
    app_path = REPO_ROOT / "app.py"
    source = app_path.read_text(encoding="utf-8")

    assert app_path.exists()
    assert "streamlit" in source
    assert "ParalegalAgentWorkflow" in source
