from fastapi import FastAPI
from pydantic import BaseModel

from app.core.config import AppSettings, load_settings
from app.core.response import ApiResponse


class HealthStatus(BaseModel):
    status: str
    service: str
    environment: str


def create_app(settings_override: AppSettings | None = None) -> FastAPI:
    app_settings = settings_override or load_settings()
    app = FastAPI(title=app_settings.app.name)

    @app.get("/health", response_model=ApiResponse[HealthStatus])
    def health() -> ApiResponse[HealthStatus]:
        return ApiResponse(
            success=True,
            data=HealthStatus(
                status="ok",
                service=app_settings.app.name,
                environment=app_settings.app.environment,
            ),
        )

    return app


app = create_app()
