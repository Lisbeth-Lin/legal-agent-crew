from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import DatabaseConfig, settings


def create_db_engine(config: DatabaseConfig | None = None) -> Engine:
    db_config = config or settings.database
    return create_engine(
        db_config.database_url,
        echo=db_config.echo_sql,
        pool_pre_ping=db_config.pool_pre_ping,
    )


engine = create_db_engine()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session() -> Iterator[Session]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
