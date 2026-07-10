install:
	uv sync --frozen

run-api:
	uv run uvicorn app.main:create_app --factory --reload

run-frontend:
	uv run streamlit run app.py

test:
	uv run pytest -q -m "not integration and not e2e and not external"

lint:
	uv run ruff check app tests

format:
	uv run ruff format app tests
