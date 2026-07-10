from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.base import Base


class BaseRepository[ModelT: Base]:
    def __init__(self, session: Session, model: type[ModelT], id_field: str) -> None:
        self.session = session
        self.model = model
        self.id_field = id_field

    def create(self, **values: Any) -> ModelT:
        instance = self.model(**values)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get_by_id(self, item_id: str) -> ModelT | None:
        return self.session.get(self.model, item_id)

    def list(self, limit: int = 100, offset: int = 0) -> list[ModelT]:
        statement = select(self.model).offset(offset).limit(limit)
        return list(self.session.scalars(statement))

    def update_status(self, item_id: str, **status_values: Any) -> ModelT | None:
        instance = self.get_by_id(item_id)
        if instance is None:
            return None
        for key, value in status_values.items():
            setattr(instance, key, value)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, item_id: str) -> bool:
        instance = self.get_by_id(item_id)
        if instance is None:
            return False
        self.session.delete(instance)
        self.session.commit()
        return True
