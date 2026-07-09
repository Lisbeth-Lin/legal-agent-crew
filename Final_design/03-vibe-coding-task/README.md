# Vibe Coding Tasks

本目录根据 `01-proposal.md` 与 `02-detailed_design` 生成，用于把 Agentic RAG 国际公法研究助手拆分为可独立开发和测试的最小任务。


## 编号规则

任务文档按推荐 Vibe Coding 编写顺序编号：

- `01-project-infrastructure.md`：01. Project Infrastructure
- `02-config-management.md`：02. Config Management Module
- `03-database-models.md`：03. Database Models Module
- `04-document-upload.md`：04. Document Upload Module
- `05-pdf-parsing.md`：05. PDF Parsing Module
- `06-knowledge-base-management.md`：06. Knowledge Base Management Module
- `07-indexing.md`：07. Indexing Module
- `08-hybrid-retrieval.md`：08. Hybrid Retrieval Module
- `09-query-classifier.md`：09. Query Classifier Module
- `10-query-rewrite.md`：10. Query Rewrite Module
- `11-evidence-pack-builder.md`：11. Evidence Pack Builder Module
- `12-answerability-evaluator.md`：12. Answerability Evaluator Module
- `13-trusted-web-search.md`：13. Trusted Web Search Module
- `14-legal-reasoning-generator.md`：14. Legal Reasoning Generator Module
- `15-citation-verification.md`：15. Citation Verification Module
- `16-evaluation.md`：16. Evaluation Module
- `17-logging-observability.md`：17. Logging and Observability Module
- `18-langgraph-workflow.md`：18. LangGraph Workflow Module
- `19-mcp-style-tools.md`：19. MCP-style Tools Module
- `20-fastapi-backend.md`：20. FastAPI Backend Module
- `21-streamlit-frontend.md`：21. Streamlit Frontend Module
- `22-business-functions.md`：22. Business Functions Module
- `23-testing-quality.md`：23. Testing and Quality Module
- `24-docker-deployment.md`：24. Docker Deployment Module

优先查看：

- `progress.md`：总体进度与推荐执行顺序。
- 每个带编号的 `<order>-<module-name>.md`：对应模块的任务 checklist、独立测试和完成标准。

约束：

1. Streamlit 只作为演示前端，核心逻辑放在 FastAPI 后端。
2. PostgreSQL 保存业务数据；Milvus 只保存向量索引；Elasticsearch 只保存 BM25 全文索引。
3. 最终答案必须基于 Evidence Pack 或可信联网证据，不允许模型自由编造 citation。
4. 每个模块应能独立测试。
