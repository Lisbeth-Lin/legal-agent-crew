\# AGENTS.md



\## Project



This repository implements the PublicLaw Research Agent.



Before making changes, read:



\- `Final_design/01-proposal.md`

\- `Final_design/02-detailed\_design.md`

\- `Final_design/03-vibe-coding-task/README.md`

\- `Final_design/03-vibe-coding-task/progress.md`

\- `Final_design/04-implementation-blueprint.md`



\## Architecture Rules



\- FastAPI contains all backend business logic.

\- Streamlit is only a demonstration frontend and communicates through HTTP/JSON.

\- PostgreSQL is the business source of truth.

\- Milvus stores only vector indexes.

\- Elasticsearch stores only BM25 indexes.

\- All LLM calls must use the shared OpenAI-compatible provider.

\- Answers may cite only the current Evidence Pack or trusted web evidence.

\- Do not delete or overwrite legacy prototype code without an explicit migration.



\## Development Rules



\- Use `uv` for dependency management.

\- Keep `pyproject.toml` and `uv.lock` synchronized.

\- New production code must have complete type annotations.

\- Every implementation task must include pytest tests.

\- New or modified code must pass ruff and mypy.

\- Do not weaken quality checks to make tests pass.

\- Never commit API keys, credentials, local databases, indexes, or generated PDF data.



\## Required Checks



Run checks appropriate to the changed scope:



```bash

uv sync --frozen

uv run ruff format --check <changed-paths>

uv run ruff check <changed-paths>

uv run mypy <changed-modules>

uv run pytest -q <relevant-tests>

