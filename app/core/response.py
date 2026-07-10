from typing import TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class ErrorBody(BaseModel):
    code: str
    message: str
    details: dict[str, object] = Field(default_factory=dict)


class ApiResponse[DataT](BaseModel):
    success: bool
    data: DataT | None = None
    error: ErrorBody | None = None
    trace_id: str | None = None


class PageParams(BaseModel):
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)


class PageResult[DataT](BaseModel):
    items: list[DataT]
    page: int
    page_size: int
    total: int
