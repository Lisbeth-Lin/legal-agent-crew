# Assumptions

## W0 assumptions

- `Final_design/` is an untracked design handoff directory supplied by the user; W0 may update its progress, docs, and reports files but should not rewrite the source design files.
- `firecrawl_note.txt` is an unrelated untracked user note and is not modified.
- There is no repository-level `AGENTS.md` file in this checkout; the user-provided AGENTS instructions in the prompt are treated as the active agent guidance.
- The current application is a Streamlit/CrewAI/Milvus Lite prototype, not the final FastAPI/LangGraph architecture.
- Because no FastAPI app exists yet, a real `/health` smoke test cannot be added without entering W1.
- Existing quality failures should be recorded as baseline issues rather than fixed by broad refactors in W0.
- Network and Windows sandbox constraints may require uv commands to run outside the sandbox with approval.

## W1 assumptions

- The user-created root `AGENTS.md` unlocks W1 and is now the active repository instruction file.
- Keeping the root Streamlit `app.py` in place is safer than moving it during W1; future frontend migration should be explicit.
- SQLite is acceptable for W1 unit tests and local migration smoke; PostgreSQL remains the target business database through `DATABASE_URL`.
- W1 repositories are intentionally minimal. Specialized repositories should be added when downstream modules need custom queries.
- W1 tests pin the repository root in `tests/conftest.py` so pytest and Alembic subprocesses can import the new `app/` package reliably on Windows.
