# Progress：Agentic RAG 国际公法研究助手 Vibe Coding 总体进度

> 说明：每个模块对应一个独立 `<module-name>.md` 文件。模块内任务全部完成并通过测试后，再勾选本文件对应模块。

## W0 Baseline Status

- [x] W0 repository preflight completed on 2026-07-10.
- [x] Existing prototype, README, pyproject, task docs, and git status inspected.
- [x] pytest markers and smoke-test directory baseline added.
- [x] ruff, mypy, pytest, and coverage configuration added.
- [ ] FastAPI `/health` smoke is not available yet because the FastAPI app belongs to W1.
- [x] W1 accepted for foundation work after root `AGENTS.md` was added.

## W1 Foundation Status

- [x] FastAPI backend package and `/health` route added.
- [x] YAML + `.env` configuration loader added.
- [x] SQLAlchemy W1 table contract and initial Alembic migration added.
- [x] Generic repository, document repository, background task repository, and task service added.
- [x] Shared response, trace context, local trace logging, and error logging contracts added.
- [x] LLM provider protocol, fake provider, OpenAI-compatible provider shell, and prompt registry added.
- [x] W1 changed-scope ruff, mypy, pytest, coverage, compileall, and Alembic smoke checks pass.
- [ ] Full 01/02/03/17 task checklists are not globally checked yet because legacy migration, specialized repositories, full API logging surfaces, and optional Langfuse integration remain deferred.
- [ ] W2 is partially unlocked only for work that depends on the W1 foundation contracts listed above.

## 1. 总体模块进度

- [ ] 01. [Project Infrastructure](./01-project-infrastructure.md)
- [ ] 02. [Config Management Module](./02-config-management.md)
- [ ] 03. [Database Models Module](./03-database-models.md)
- [ ] 04. [Document Upload Module](./04-document-upload.md)
- [ ] 05. [PDF Parsing Module](./05-pdf-parsing.md)
- [ ] 06. [Knowledge Base Management Module](./06-knowledge-base-management.md)
- [ ] 07. [Indexing Module](./07-indexing.md)
- [ ] 08. [Hybrid Retrieval Module](./08-hybrid-retrieval.md)
- [ ] 09. [Query Classifier Module](./09-query-classifier.md)
- [ ] 10. [Query Rewrite Module](./10-query-rewrite.md)
- [ ] 11. [Evidence Pack Builder Module](./11-evidence-pack-builder.md)
- [ ] 12. [Answerability Evaluator Module](./12-answerability-evaluator.md)
- [ ] 13. [Trusted Web Search Module](./13-trusted-web-search.md)
- [ ] 14. [Legal Reasoning Generator Module](./14-legal-reasoning-generator.md)
- [ ] 15. [Citation Verification Module](./15-citation-verification.md)
- [ ] 16. [Evaluation Module](./16-evaluation.md)
- [ ] 17. [Logging and Observability Module](./17-logging-observability.md)
- [ ] 18. [LangGraph Workflow Module](./18-langgraph-workflow.md)
- [ ] 19. [MCP-style Tools Module](./19-mcp-style-tools.md)
- [ ] 20. [FastAPI Backend Module](./20-fastapi-backend.md)
- [ ] 21. [Streamlit Frontend Module](./21-streamlit-frontend.md)
- [ ] 22. [Business Functions Module](./22-business-functions.md)
- [ ] 23. [Testing and Quality Module](./23-testing-quality.md)
- [ ] 24. [Docker Deployment Module](./24-docker-deployment.md)

## 2. 推荐执行顺序

### Phase 1：原型工程化改造

- [ ] [Project Infrastructure](./01-project-infrastructure.md)
- [ ] [Config Management Module](./02-config-management.md)
- [ ] [Database Models Module](./03-database-models.md)
- [ ] [Document Upload Module](./04-document-upload.md)
- [ ] [FastAPI Backend Module](./20-fastapi-backend.md)
- [ ] [Streamlit Frontend Module](./21-streamlit-frontend.md)

### Phase 2：PDF 解析与引用增强

- [ ] [PDF Parsing Module](./05-pdf-parsing.md)
- [ ] [Knowledge Base Management Module](./06-knowledge-base-management.md)
- [ ] [Citation Verification Module](./15-citation-verification.md)

### Phase 3：Hybrid Retrieval 升级

- [ ] [Indexing Module](./07-indexing.md)
- [ ] [Hybrid Retrieval Module](./08-hybrid-retrieval.md)
- [ ] [Evidence Pack Builder Module](./11-evidence-pack-builder.md)

### Phase 4：LangGraph Agentic RAG

- [ ] [Query Classifier Module](./09-query-classifier.md)
- [ ] [Query Rewrite Module](./10-query-rewrite.md)
- [ ] [Answerability Evaluator Module](./12-answerability-evaluator.md)
- [ ] [Trusted Web Search Module](./13-trusted-web-search.md)
- [ ] [Legal Reasoning Generator Module](./14-legal-reasoning-generator.md)
- [ ] [LangGraph Workflow Module](./18-langgraph-workflow.md)
- [ ] [MCP-style Tools Module](./19-mcp-style-tools.md)
- [ ] [Business Functions Module](./22-business-functions.md)

### Phase 5：评测、观测与交付

- [ ] [Evaluation Module](./16-evaluation.md)
- [ ] [Logging and Observability Module](./17-logging-observability.md)
- [ ] [Testing and Quality Module](./23-testing-quality.md)
- [ ] [Docker Deployment Module](./24-docker-deployment.md)

## 3. 里程碑验收

- [ ] M1：FastAPI + Streamlit 前后端分离跑通，/health 和 /documents/upload 可用。
- [ ] M2：PDF 能解析为 page、chunk、citation_anchor，并保存到 PostgreSQL。
- [ ] M3：Milvus + Elasticsearch 索引构建完成，Hybrid Retrieval 可返回证据。
- [ ] M4：LangGraph 完整问答链路跑通，能输出英文 IRAC + Sources。
- [ ] M5：Citation Verification、RAGAS、自定义指标和 Langfuse 日志可展示。
- [ ] M6：Docker Compose 一键启动演示环境，README 可复现。
