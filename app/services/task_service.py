from sqlalchemy.orm import Session

from app.db.models import BackgroundTask, utc_now
from app.repositories.tasks import BackgroundTaskRepository

TERMINAL_TASK_STATUSES = {"success", "failed", "cancelled"}


class TaskService:
    def __init__(self, session: Session) -> None:
        self.repository = BackgroundTaskRepository(session)

    def create_task(
        self,
        task_type: str,
        target_id: str,
        payload: dict[str, object] | None = None,
    ) -> BackgroundTask:
        return self.repository.create(
            task_type=task_type,
            target_id=target_id,
            payload=payload or {},
            status="pending",
            progress=0.0,
        )

    def mark_running(self, task_id: str) -> BackgroundTask | None:
        return self.repository.update_status(
            task_id,
            status="running",
            started_at=utc_now(),
            progress=0.0,
        )

    def mark_success(self, task_id: str) -> BackgroundTask | None:
        return self.repository.update_status(
            task_id,
            status="success",
            progress=1.0,
            finished_at=utc_now(),
        )

    def mark_failed(self, task_id: str, message: str) -> BackgroundTask | None:
        return self.repository.update_status(
            task_id,
            status="failed",
            error_message=message,
            finished_at=utc_now(),
        )

    def cancel(self, task_id: str) -> BackgroundTask | None:
        task = self.repository.get_by_id(task_id)
        if task is None or task.status in TERMINAL_TASK_STATUSES:
            return task
        return self.repository.update_status(
            task_id,
            status="cancelled",
            finished_at=utc_now(),
        )
