# Decisions

## 2026-07-10 - W0 quality baseline only

- Scope is limited to W0 from `Final_design/04-implementation-blueprint.md`.
- Existing Streamlit prototype code is preserved in place for W0. It is not moved to `legacy/` yet because that would be a structural source migration and belongs to W1 or later.
- The repository already uses `pyproject.toml` and `uv.lock`, so W0 keeps uv rather than migrating package management.
- Python remains 3.13 for W0 because the current project metadata declares `requires-python = ">=3.13"` and the existing lock/environment were built around that line.
- Quality tooling is added through a `dev` dependency group: pytest, pytest-cov, mypy, and ruff.
- Default pytest scope is non-external and marker-aware. Integration, e2e, external, slow, and ocr markers are declared but not exercised by the W0 smoke test.
- Coverage source is limited to current production packages `config` and `src`. The future `app/` package is not configured yet because it does not exist in the W0 repository.
- W0 smoke tests intentionally avoid importing heavy ML, Milvus, Streamlit runtime state, or external API clients.

## Deferred to W1

- Create final `app/` FastAPI layout and `/health` route.
- Move or wrap the Streamlit prototype under `legacy/` or `frontend/legacy/`.
- Freeze shared schemas, API response contracts, database models, and provider protocols.
- Add Docker Compose development services.

## 2026-07-10 - W1 foundation package

- W1 is implemented as a new `app/` backend package while preserving the existing root `app.py` Streamlit prototype.
- The prototype is documented under `frontend/legacy/README.md` but not moved, because `AGENTS.md` forbids deleting or overwriting legacy prototype code without an explicit migration.
- FastAPI exposes `/health` from `app/main.py`.
- Configuration is loaded from `config/*.yaml` plus `.env`, with tests using explicit overrides.
- SQLAlchemy 2.0 models define the W1 business-source-of-truth tables, including documents, pages, chunks, citations, tasks, aliases, trusted web sources, prompt versions, QA logs, retrieval logs, model runs, trace logs, evaluation logs, feedback, and errors.
- The initial Alembic migration delegates to SQLAlchemy metadata for W1. This keeps the first schema consistent with the models; later migrations should use explicit operations when schema changes stabilize.
- W1 adds a generic repository plus document and background-task repositories. Per-table specialized repositories remain deferred until each downstream module needs table-specific behavior.
- The LLM boundary is a protocol plus deterministic fake provider and an OpenAI-compatible provider shell. Real network generation remains deferred until reasoning/generator modules use it.
- Local trace/error logging is implemented against SQLAlchemy models. Langfuse integration remains optional and deferred behind the configured `enable_langfuse` flag.
