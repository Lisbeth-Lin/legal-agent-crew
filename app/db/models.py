from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import JSON, Boolean, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


def new_id() -> str:
    return uuid4().hex


def utc_now() -> datetime:
    return datetime.now(UTC)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(default=utc_now, onupdate=utc_now)


class Document(Base, TimestampMixin):
    __tablename__ = "documents"

    doc_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    title: Mapped[str] = mapped_column(Text)
    institution: Mapped[str | None] = mapped_column(String(255))
    year: Mapped[int | None] = mapped_column(Integer)
    legal_domain: Mapped[str | None] = mapped_column(String(255))
    document_type: Mapped[str] = mapped_column(String(64), default="case_report")
    language: Mapped[str] = mapped_column(String(16), default="en")
    source_url: Mapped[str | None] = mapped_column(Text)
    file_path: Mapped[str | None] = mapped_column(Text)
    file_hash: Mapped[str | None] = mapped_column(String(128), unique=True)
    upload_time: Mapped[datetime] = mapped_column(default=utc_now)
    parse_status: Mapped[str] = mapped_column(String(32), default="not_started")
    index_status: Mapped[str] = mapped_column(String(32), default="not_indexed")

    pages: Mapped[list["DocumentPage"]] = relationship(
        back_populates="document", cascade="all, delete-orphan"
    )
    chunks: Mapped[list["DocumentChunk"]] = relationship(
        back_populates="document", cascade="all, delete-orphan"
    )


class DocumentPage(Base, TimestampMixin):
    __tablename__ = "document_pages"

    page_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    doc_id: Mapped[str] = mapped_column(ForeignKey("documents.doc_id", ondelete="CASCADE"))
    pdf_page_number: Mapped[int] = mapped_column(Integer)
    printed_page_number: Mapped[str | None] = mapped_column(String(64))
    citation_page_number: Mapped[str | None] = mapped_column(String(64))
    text: Mapped[str] = mapped_column(Text)
    cleaned_text: Mapped[str | None] = mapped_column(Text)
    source_type: Mapped[str] = mapped_column(String(32), default="pdf_text")
    parse_status: Mapped[str] = mapped_column(String(32), default="success")
    header_footer_removed: Mapped[bool] = mapped_column(Boolean, default=False)
    error_message: Mapped[str | None] = mapped_column(Text)

    document: Mapped[Document] = relationship(back_populates="pages")


class DocumentChunk(Base, TimestampMixin):
    __tablename__ = "document_chunks"

    chunk_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    doc_id: Mapped[str] = mapped_column(ForeignKey("documents.doc_id", ondelete="CASCADE"))
    page_id: Mapped[str | None] = mapped_column(ForeignKey("document_pages.page_id"))
    title: Mapped[str] = mapped_column(Text)
    pdf_page_number: Mapped[int | None] = mapped_column(Integer)
    printed_page_number: Mapped[str | None] = mapped_column(String(64))
    citation_page_number: Mapped[str | None] = mapped_column(String(64))
    paragraph_number: Mapped[str | None] = mapped_column(String(64))
    paragraph_number_confidence: Mapped[float | None] = mapped_column(Float)
    section_title: Mapped[str | None] = mapped_column(Text)
    text: Mapped[str] = mapped_column(Text)
    original_sentence: Mapped[str | None] = mapped_column(Text)
    footnote_text: Mapped[str | None] = mapped_column(Text)
    citation_anchor: Mapped[str] = mapped_column(String(255), unique=True)
    source_type: Mapped[str] = mapped_column(String(32), default="pdf_text")
    token_count: Mapped[int | None] = mapped_column(Integer)
    embedding_id: Mapped[str | None] = mapped_column(String(128))
    bm25_id: Mapped[str | None] = mapped_column(String(128))

    document: Mapped[Document] = relationship(back_populates="chunks")


class CitationAnchor(Base, TimestampMixin):
    __tablename__ = "citation_anchors"

    citation_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    chunk_id: Mapped[str | None] = mapped_column(ForeignKey("document_chunks.chunk_id"))
    doc_id: Mapped[str | None] = mapped_column(ForeignKey("documents.doc_id"))
    title: Mapped[str] = mapped_column(Text)
    citation_page_number: Mapped[str | None] = mapped_column(String(64))
    pdf_page_number: Mapped[int | None] = mapped_column(Integer)
    paragraph_number: Mapped[str | None] = mapped_column(String(64))
    original_sentence: Mapped[str | None] = mapped_column(Text)
    snippet: Mapped[str | None] = mapped_column(Text)
    citation_anchor: Mapped[str] = mapped_column(String(255), unique=True)
    source_url: Mapped[str | None] = mapped_column(Text)
    source_channel: Mapped[str] = mapped_column(String(32), default="local_pdf")
    trust_level: Mapped[str | None] = mapped_column(String(32))


class BackgroundTask(Base, TimestampMixin):
    __tablename__ = "background_tasks"

    task_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    task_type: Mapped[str] = mapped_column(String(64))
    target_id: Mapped[str] = mapped_column(String(64))
    payload: Mapped[dict[str, object]] = mapped_column(JSON, default=dict)
    status: Mapped[str] = mapped_column(String(32), default="pending")
    progress: Mapped[float] = mapped_column(Float, default=0.0)
    retry_count: Mapped[int] = mapped_column(Integer, default=0)
    error_message: Mapped[str | None] = mapped_column(Text)
    started_at: Mapped[datetime | None] = mapped_column()
    finished_at: Mapped[datetime | None] = mapped_column()


class CaseAlias(Base, TimestampMixin):
    __tablename__ = "case_aliases"

    alias_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    canonical_name: Mapped[str] = mapped_column(Text)
    alias: Mapped[str] = mapped_column(Text)
    source: Mapped[str | None] = mapped_column(String(255))


class TrustedWebSource(Base, TimestampMixin):
    __tablename__ = "trusted_web_sources"

    source_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    domain: Mapped[str] = mapped_column(String(255), unique=True)
    trust_level: Mapped[str] = mapped_column(String(32))
    institution: Mapped[str | None] = mapped_column(String(255))
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)


class WebEvidence(Base, TimestampMixin):
    __tablename__ = "web_evidence"

    evidence_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    trace_id: Mapped[str] = mapped_column(String(128))
    url: Mapped[str] = mapped_column(Text)
    title: Mapped[str | None] = mapped_column(Text)
    snippet: Mapped[str | None] = mapped_column(Text)
    source_domain: Mapped[str] = mapped_column(String(255))
    trust_level: Mapped[str | None] = mapped_column(String(32))


class PromptVersion(Base, TimestampMixin):
    __tablename__ = "prompt_versions"

    prompt_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    name: Mapped[str] = mapped_column(String(128))
    version: Mapped[str] = mapped_column(String(64))
    prompt_hash: Mapped[str] = mapped_column(String(128))
    template: Mapped[str] = mapped_column(Text)


class QASession(Base, TimestampMixin):
    __tablename__ = "qa_sessions"

    session_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    title: Mapped[str | None] = mapped_column(Text)


class QAMessage(Base, TimestampMixin):
    __tablename__ = "qa_messages"

    message_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    session_id: Mapped[str | None] = mapped_column(ForeignKey("qa_sessions.session_id"))
    trace_id: Mapped[str] = mapped_column(String(128))
    role: Mapped[str] = mapped_column(String(32))
    content: Mapped[str] = mapped_column(Text)
    answerability: Mapped[str | None] = mapped_column(String(64))


class RetrievalResult(Base, TimestampMixin):
    __tablename__ = "retrieval_results"

    result_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    trace_id: Mapped[str] = mapped_column(String(128))
    chunk_id: Mapped[str | None] = mapped_column(ForeignKey("document_chunks.chunk_id"))
    source_channel: Mapped[str] = mapped_column(String(32), default="local_pdf")
    bm25_score: Mapped[float | None] = mapped_column(Float)
    vector_score: Mapped[float | None] = mapped_column(Float)
    fused_score: Mapped[float | None] = mapped_column(Float)
    rerank_score: Mapped[float | None] = mapped_column(Float)
    rank: Mapped[int | None] = mapped_column(Integer)


class AnswerCitation(Base, TimestampMixin):
    __tablename__ = "answer_citations"

    answer_citation_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    message_id: Mapped[str | None] = mapped_column(ForeignKey("qa_messages.message_id"))
    citation_id: Mapped[str | None] = mapped_column(ForeignKey("citation_anchors.citation_id"))
    citation_anchor: Mapped[str] = mapped_column(String(255))
    verification_status: Mapped[str] = mapped_column(String(32), default="pending")


class ModelRun(Base, TimestampMixin):
    __tablename__ = "model_runs"

    run_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    trace_id: Mapped[str] = mapped_column(String(128))
    provider: Mapped[str] = mapped_column(String(64))
    model: Mapped[str] = mapped_column(String(128))
    prompt_name: Mapped[str | None] = mapped_column(String(128))
    prompt_version: Mapped[str | None] = mapped_column(String(64))
    usage: Mapped[dict[str, object]] = mapped_column(JSON, default=dict)
    status: Mapped[str] = mapped_column(String(32), default="success")


class TraceLog(Base, TimestampMixin):
    __tablename__ = "trace_logs"

    log_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    trace_id: Mapped[str] = mapped_column(String(128), index=True)
    event_type: Mapped[str] = mapped_column(String(128))
    payload: Mapped[dict[str, object]] = mapped_column(JSON, default=dict)


class EvaluationLog(Base, TimestampMixin):
    __tablename__ = "evaluation_logs"

    evaluation_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    trace_id: Mapped[str] = mapped_column(String(128))
    metrics: Mapped[dict[str, object]] = mapped_column(JSON, default=dict)
    status: Mapped[str] = mapped_column(String(32), default="success")


class FeedbackLog(Base, TimestampMixin):
    __tablename__ = "feedback_logs"

    feedback_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    message_id: Mapped[str] = mapped_column(String(64))
    rating: Mapped[int] = mapped_column(Integer)
    feedback_type: Mapped[str] = mapped_column(String(64))
    comment: Mapped[str | None] = mapped_column(Text)


class ErrorLog(Base, TimestampMixin):
    __tablename__ = "error_logs"

    error_id: Mapped[str] = mapped_column(String(64), primary_key=True, default=new_id)
    trace_id: Mapped[str | None] = mapped_column(String(128), index=True)
    module: Mapped[str] = mapped_column(String(128))
    error_type: Mapped[str] = mapped_column(String(128))
    message: Mapped[str] = mapped_column(Text)
    stacktrace: Mapped[str | None] = mapped_column(Text)
