from uuid import uuid4

from pydantic import BaseModel, Field


def new_trace_id() -> str:
    return f"trace_{uuid4().hex}"


class TraceContext(BaseModel):
    trace_id: str = Field(default_factory=new_trace_id)
    session_id: str | None = None
    message_id: str | None = None
