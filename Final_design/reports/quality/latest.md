# W0 Quality Baseline

Date: 2026-07-10

## Scope

W0 only. No W1 implementation started.

## Repository baseline

- Branch: `main`
- Tracking: `main...origin/main`
- Git status before edits: untracked `Final_design/`, untracked `firecrawl_note.txt`
- Repository-level `AGENTS.md`: not present
- Existing prototype entrypoint: `app.py`
- Existing package management: `pyproject.toml` plus `uv.lock`
- Existing tests directory before W0: not present

## Quality configuration added

- pytest markers: `unit`, `integration`, `e2e`, `external`, `slow`, `ocr`
- pytest discovery: `tests`
- coverage source: `config`, `src`
- mypy: strict mode, Python 3.13, scoped third-party import overrides
- ruff: Python 3.13 target, line length 100, lint families from the implementation blueprint

## Commands

- `git status --short --branch`
  - Result: pass
  - Output: `## main...origin/main`, untracked `Final_design/`, untracked `firecrawl_note.txt`
- `git diff -- pyproject.toml README.md app.py config src examples`
  - Result: pass
  - Output: no tracked user edits before W0 changes
- `uv --version`
  - Result: pass
  - Output: `uv 0.11.26`
- `uv lock`
  - Result: pass
  - Output: resolved 260 packages; added pytest, pytest-cov, mypy, ruff, coverage and transitive dev dependencies
- `uv sync --frozen`
  - Result: pass
  - Output: installed 10 dev packages; warning only for hardlink fallback to full copy
- `uv run python --version`
  - Result: pass
  - Output: `Python 3.13.14`
- `uv run pytest -q -m "not integration and not e2e and not external"`
  - Result: pass
  - Output: `2 passed`
- `uv run pytest --cov=config --cov=src --cov-branch --cov-report=term-missing -m "not integration and not e2e and not external"`
  - Result: pass with baseline warning
  - Output: `2 passed`; coverage reported `config/settings.py` at 0% and warned that no production-code data was collected
- `uv run ruff format --check .`
  - Result: fail, existing formatting baseline
  - Output: 10 existing files would be reformatted: `app.py`, `config/settings.py`, `examples/test.py`, and 7 files under `src/`
- `uv run ruff check . --statistics`
  - Result: fail, existing lint baseline
  - Output: 132 lint findings after W0 test cleanup; largest groups are E402, UP045, E501, RUF013, I001, UP006
- `uv run ruff check tests`
  - Result: pass
  - Output: W0-added tests pass lint
- `uv run ruff format --check tests Final_design\docs Final_design\reports`
  - Result: pass
  - Output: W0-added Python test file already formatted
- `uv run mypy app.py config src tests`
  - Result: fail, existing type baseline
  - Output: 76 errors across 9 files; examples include missing return annotations, implicit Optional defaults, untyped decorators, and third-party Any base classes
- `uv run python -m compileall -q app.py config examples src tests`
  - Result: pass
  - Output: current Python 3.13 syntax compiles

## Current known issues

- No FastAPI app or `/health` route exists yet.
- Coverage is only a baseline: the W0 smoke tests avoid importing production modules, so production coverage is effectively 0%.
- Existing source files do not pass strict ruff format, ruff lint, or mypy.
- `examples/test.py` uses Python 3.12+ f-string syntax and compiles under the W0 Python 3.13.14 baseline.
- The design markdown files display mojibake in some PowerShell `Get-Content` reads, although targeted `Select-String` output can display Chinese correctly.

## W1 unlock status

Not unlocked yet.

Reasons:

- `/health` smoke cannot run until the FastAPI app is created.
- Full ruff and mypy gates fail on existing prototype code.
- Coverage is not meaningful beyond W0 smoke-test discovery.

Allowed next step:

- Start W1 only after accepting this W0 baseline or first deciding whether W1 should fix quality debt before building new architecture.

---

# W1 Quality Baseline

Date: 2026-07-10

## Scope

W1 foundation only. No W2 ingestion, parsing, indexing, retrieval, or generation work started.

## Implemented W1 surface

- New FastAPI backend package under `app/`
- `/health` endpoint
- YAML + `.env` configuration loader and schemas
- SQLAlchemy business tables and initial Alembic migration
- Generic repository plus document/background-task repositories
- Task status service
- Trace context, trace logging, and error logging services
- LLM provider protocol, fake provider, OpenAI-compatible provider shell, and prompt registry
- W1 unit tests for config, health, database, task service, logging, and LLM boundaries

## Commands

- `uv lock`
  - Result: pass
  - Output: resolved 277 packages; added W1 dependencies including Alembic, SQLAlchemy, FastAPI stack, PyYAML, PyMuPDF, Elasticsearch, LangGraph, RAGAS, Langfuse, and psycopg
- `uv sync --frozen`
  - Result: pass
  - Output: checked 256 packages
- `uv run ruff format --check app tests migrations`
  - Result: pass
  - Output: 36 files already formatted
- `uv run ruff check app tests migrations`
  - Result: pass
  - Output: all checks passed
- `uv run mypy app tests/conftest.py tests/unit/test_w1_config.py tests/unit/test_w1_health.py tests/unit/test_w1_database.py tests/unit/test_w1_logging.py tests/unit/test_w1_llm.py`
  - Result: pass
  - Output: no issues found in 33 source files; mypy noted unused legacy third-party override sections
- `uv run pytest -q tests/unit/test_w0_smoke.py tests/unit/test_w1_config.py tests/unit/test_w1_health.py tests/unit/test_w1_database.py tests/unit/test_w1_logging.py tests/unit/test_w1_llm.py`
  - Result: pass
  - Output: 17 passed
- `uv run pytest --cov=app --cov-branch --cov-report=term-missing tests/unit/test_w1_config.py tests/unit/test_w1_health.py tests/unit/test_w1_database.py tests/unit/test_w1_logging.py tests/unit/test_w1_llm.py`
  - Result: pass
  - Output: 15 passed, app coverage 92%
- `uv run python -m compileall -q app tests migrations`
  - Result: pass
- `DATABASE_URL=sqlite:///:memory: uv run alembic upgrade head`
  - Result: pass
  - Output: upgraded to `0001_initial_schema`

## Current known issues

- Full-repository ruff/mypy still fail on legacy prototype code from the W0 baseline; W1 changed-scope gates pass.
- Root `AGENTS.md` contains escaped Markdown characters, but the rules are readable and were followed.
- `app/db/session.py` is configured but not covered by W1 tests because tests inject in-memory SQLite sessions directly.
- Real OpenAI-compatible network generation is intentionally not implemented in W1.
- Langfuse client integration is deferred; local trace/error logging is implemented.

## W2 unlock status

Partially unlocked.

W2 can start for modules that depend on:

- FastAPI app creation and `/health`
- config loader and YAML contract
- SQLAlchemy models and migration baseline
- task service foundation
- fake LLM provider for deterministic tests
- local trace/error logging

W2 should not assume:

- specialized repositories exist for every table
- Streamlit has been migrated away from root `app.py`
- external services are running
- real LLM, Milvus, Elasticsearch, Firecrawl, or Langfuse integrations are complete
