from collections.abc import Iterator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import app.db.models  # noqa: F401
from app.core.tracing import TraceContext
from app.db.base import Base
from app.services.logging_service import ErrorLoggingService, LoggingService


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
def test_trace_context_generates_trace_id() -> None:
    context = TraceContext()

    assert context.trace_id.startswith("trace_")


@pytest.mark.unit
def test_logging_service_writes_trace_event(db_session: Session) -> None:
    event = LoggingService(db_session).log_event(
        trace_id="trace_test",
        event_type="retrieval",
        payload={"count": 3},
    )

    assert event.trace_id == "trace_test"
    assert event.payload["count"] == 3


@pytest.mark.unit
def test_error_logging_service_writes_error(db_session: Session) -> None:
    context = TraceContext(trace_id="trace_error")

    error = ErrorLoggingService(db_session).log_error(
        module="unit-test",
        error=ValueError("bad input"),
        trace_context=context,
    )

    assert error.trace_id == "trace_error"
    assert error.error_type == "ValueError"
    assert "bad input" in error.message
