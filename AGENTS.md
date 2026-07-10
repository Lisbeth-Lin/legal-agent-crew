# AGENTS.md

## Project

This repository implements the PublicLaw Research Agent.

Before making changes, read:

- `Final_design/01-proposal.md`
- `Final_design/02-detailed_design.md`
- `Final_design/03-vibe-coding-task/README.md`
- `Final_design/03-vibe-coding-task/progress.md`
- `Final_design/04-implementation-blueprint.md`

## Architecture Rules

- FastAPI contains all backend business logic.
- Streamlit is only a demonstration frontend and communicates through HTTP/JSON.
- PostgreSQL is the business source of truth.
- Milvus stores only vector indexes.
- Elasticsearch stores only BM25 indexes.
- All LLM calls must use the shared OpenAI-compatible provider.
- Answers may cite only the current Evidence Pack or trusted web evidence.
- Do not delete or overwrite legacy prototype code without an explicit migration.

## Development Rules

- Use `uv` for dependency management.
- Keep `pyproject.toml` and `uv.lock` synchronized.
- New production code must have complete type annotations.
- Every implementation task must include pytest tests.
- New or modified code must pass ruff and mypy.
- Do not weaken quality checks to make tests pass.
- Never commit API keys, credentials, local databases, indexes, or generated PDF data.
- Preserve existing user work. Stage only files that belong to the current task.

## Required Checks

Run checks appropriate to the changed scope:

```bash
uv sync --frozen
uv run ruff format --check <changed-paths>
uv run ruff check <changed-paths>
uv run mypy <changed-modules>
uv run pytest -q <relevant-tests>
```

For W0/W1 foundation work, the current changed-scope gate is:

```bash
uv sync --frozen
uv run ruff format --check app tests migrations
uv run ruff check app tests migrations
uv run mypy app tests/conftest.py tests/unit/test_w1_config.py tests/unit/test_w1_health.py tests/unit/test_w1_database.py tests/unit/test_w1_logging.py tests/unit/test_w1_llm.py
uv run pytest -q tests/unit/test_w0_smoke.py tests/unit/test_w1_config.py tests/unit/test_w1_health.py tests/unit/test_w1_database.py tests/unit/test_w1_logging.py tests/unit/test_w1_llm.py
uv run python -m compileall -q app tests migrations
```

Before publishing a PR, also run:

```bash
git diff --check main...HEAD
```

## Wave Gates

- Do not start W1 until W0 records repository preflight, quality baseline, assumptions, and known failures.
- Do not start W2 until W1 provides a working FastAPI app, `/health`, configuration loading, database contracts, task foundation, fake LLM provider, and local trace/error logging.
- Do not start W3 until upload, parsing, citation anchors, indexing inputs, and knowledge-base management contracts are available.
- Do not start W4 until retrieval, normalization, query classification, query rewrite, and Evidence Pack construction are testable with fakes.
- Do not start W5 until answerability, trusted web fallback, legal reasoning generation, citation verification, evaluation, and logging foundations are testable.
- Do not start W6 until workflow/tool integration is stable enough for API and Streamlit surfaces.
- Each wave must update `Final_design/03-vibe-coding-task/progress.md`, `Final_design/docs/decisions.md`, `Final_design/docs/assumptions.md`, and `Final_design/reports/quality/latest.md`.

## Legacy Prototype

- The root `app.py` is the preserved Streamlit/CrewAI prototype.
- New backend work belongs under `app/`.
- Future Streamlit work should live under `frontend/` and call FastAPI through HTTP/JSON.
- Moving or deleting the prototype requires an explicit migration task.
