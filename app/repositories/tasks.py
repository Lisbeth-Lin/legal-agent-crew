from sqlalchemy.orm import Session

from app.db.models import BackgroundTask
from app.repositories.base import BaseRepository


class BackgroundTaskRepository(BaseRepository[BackgroundTask]):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, model=BackgroundTask, id_field="task_id")
