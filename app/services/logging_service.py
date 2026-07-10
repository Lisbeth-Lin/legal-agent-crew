import traceback

from sqlalchemy.orm import Session

from app.core.tracing import TraceContext
from app.db.models import ErrorLog, TraceLog


class LoggingService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def log_event(
        self,
        trace_id: str,
        event_type: str,
        payload: dict[str, object] | None = None,
    ) -> TraceLog:
        entry = TraceLog(trace_id=trace_id, event_type=event_type, payload=payload or {})
        self.session.add(entry)
        self.session.commit()
        self.session.refresh(entry)
        return entry


class ErrorLoggingService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def log_error(
        self,
        module: str,
        error: BaseException,
        trace_context: TraceContext | None = None,
    ) -> ErrorLog:
        entry = ErrorLog(
            trace_id=trace_context.trace_id if trace_context else None,
            module=module,
            error_type=type(error).__name__,
            message=str(error),
            stacktrace="".join(traceback.format_exception(error)),
        )
        self.session.add(entry)
        self.session.commit()
        self.session.refresh(entry)
        return entry
