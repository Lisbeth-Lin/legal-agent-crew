from collections.abc import Iterator

import pytest
from sqlalchemy import Engine, create_engine, inspect
from sqlalchemy.orm import Session, sessionmaker

import app.db.models  # noqa: F401
from app.db.base import Base
from app.repositories.documents import DocumentRepository
from app.services.task_service import TaskService


@pytest.fixture
def db_session() -> Iterator[Session]:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


@pytest.mark.unit
def test_w1_tables_are_created(db_session: Session) -> None:
    assert isinstance(db_session.bind, Engine)
    table_names = set(inspect(db_session.bind).get_table_names())

    assert "documents" in table_names
    assert "document_chunks" in table_names
    assert "background_tasks" in table_names
    assert "trace_logs" in table_names
    assert "error_logs" in table_names
    assert "feedback_logs" in table_names


@pytest.mark.unit
def test_document_chunk_has_document_foreign_key(db_session: Session) -> None:
    assert isinstance(db_session.bind, Engine)
    foreign_keys = inspect(db_session.bind).get_foreign_keys("document_chunks")

    assert any(fk["referred_table"] == "documents" for fk in foreign_keys)


@pytest.mark.unit
def test_document_repository_crud(db_session: Session) -> None:
    repository = DocumentRepository(db_session)

    document = repository.create(title="Nicaragua", document_type="case_report")
    fetched = repository.get_by_id(document.doc_id)
    updated = repository.update_status(document.doc_id, parse_status="success")
    deleted = repository.delete(document.doc_id)

    assert fetched is not None
    assert fetched.title == "Nicaragua"
    assert updated is not None
    assert updated.parse_status == "success"
    assert deleted is True
    assert repository.get_by_id(document.doc_id) is None


@pytest.mark.unit
def test_task_service_status_transitions(db_session: Session) -> None:
    service = TaskService(db_session)

    task = service.create_task("parse_document", "doc_1")
    running = service.mark_running(task.task_id)

    assert running is not None
    assert running.status == "running"

    success = service.mark_success(task.task_id)
    assert success is not None
    assert success.status == "success"

    cancelled = service.cancel(task.task_id)
    assert cancelled is not None
    assert cancelled.status == "success"
