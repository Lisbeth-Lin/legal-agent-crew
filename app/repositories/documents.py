from sqlalchemy.orm import Session

from app.db.models import Document
from app.repositories.base import BaseRepository


class DocumentRepository(BaseRepository[Document]):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, model=Document, id_field="doc_id")
