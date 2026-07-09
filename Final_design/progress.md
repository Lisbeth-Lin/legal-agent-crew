# Progress：Agentic RAG 国际公法研究助手 Vibe Coding 总体进度

> 说明：每个模块对应一个独立 `<module-name>.md` 文件。模块内任务全部完成并通过测试后，再勾选本文件对应模块。

## 1. 总体模块进度

- [ ] 01. [Project Infrastructure](./project-infrastructure.md)
- [ ] 02. [Config Management Module](./config-management.md)
- [ ] 03. [Database Models Module](./database-models.md)
- [ ] 04. [Document Upload Module](./document-upload.md)
- [ ] 05. [PDF Parsing Module](./pdf-parsing.md)
- [ ] 06. [Knowledge Base Management Module](./knowledge-base-management.md)
- [ ] 07. [Indexing Module](./indexing.md)
- [ ] 08. [Hybrid Retrieval Module](./hybrid-retrieval.md)
- [ ] 09. [Query Classifier Module](./query-classifier.md)
- [ ] 10. [Query Rewrite Module](./query-rewrite.md)
- [ ] 11. [Evidence Pack Builder Module](./evidence-pack-builder.md)
- [ ] 12. [Answerability Evaluator Module](./answerability-evaluator.md)
- [ ] 13. [Trusted Web Search Module](./trusted-web-search.md)
- [ ] 14. [Legal Reasoning Generator Module](./legal-reasoning-generator.md)
- [ ] 15. [Citation Verification Module](./citation-verification.md)
- [ ] 16. [Evaluation Module](./evaluation.md)
- [ ] 17. [Logging and Observability Module](./logging-observability.md)
- [ ] 18. [LangGraph Workflow Module](./langgraph-workflow.md)
- [ ] 19. [MCP-style Tools Module](./mcp-style-tools.md)
- [ ] 20. [FastAPI Backend Module](./fastapi-backend.md)
- [ ] 21. [Streamlit Frontend Module](./streamlit-frontend.md)
- [ ] 22. [Business Functions Module](./business-functions.md)
- [ ] 23. [Testing and Quality Module](./testing-quality.md)
- [ ] 24. [Docker Deployment Module](./docker-deployment.md)

## 2. 推荐执行顺序

### Phase 1：原型工程化改造

- [ ] [Project Infrastructure](./project-infrastructure.md)
- [ ] [Config Management Module](./config-management.md)
- [ ] [Database Models Module](./database-models.md)
- [ ] [Document Upload Module](./document-upload.md)
- [ ] [FastAPI Backend Module](./fastapi-backend.md)
- [ ] [Streamlit Frontend Module](./streamlit-frontend.md)

### Phase 2：PDF 解析与引用增强

- [ ] [PDF Parsing Module](./pdf-parsing.md)
- [ ] [Knowledge Base Management Module](./knowledge-base-management.md)
- [ ] [Citation Verification Module](./citation-verification.md)

### Phase 3：Hybrid Retrieval 升级

- [ ] [Indexing Module](./indexing.md)
- [ ] [Hybrid Retrieval Module](./hybrid-retrieval.md)
- [ ] [Evidence Pack Builder Module](./evidence-pack-builder.md)

### Phase 4：LangGraph Agentic RAG

- [ ] [Query Classifier Module](./query-classifier.md)
- [ ] [Query Rewrite Module](./query-rewrite.md)
- [ ] [Answerability Evaluator Module](./answerability-evaluator.md)
- [ ] [Trusted Web Search Module](./trusted-web-search.md)
- [ ] [Legal Reasoning Generator Module](./legal-reasoning-generator.md)
- [ ] [LangGraph Workflow Module](./langgraph-workflow.md)
- [ ] [MCP-style Tools Module](./mcp-style-tools.md)
- [ ] [Business Functions Module](./business-functions.md)

### Phase 5：评测、观测与交付

- [ ] [Evaluation Module](./evaluation.md)
- [ ] [Logging and Observability Module](./logging-observability.md)
- [ ] [Testing and Quality Module](./testing-quality.md)
- [ ] [Docker Deployment Module](./docker-deployment.md)

## 3. 里程碑验收

- [ ] M1：FastAPI + Streamlit 前后端分离跑通，/health 和 /documents/upload 可用。
- [ ] M2：PDF 能解析为 page、chunk、citation_anchor，并保存到 PostgreSQL。
- [ ] M3：Milvus + Elasticsearch 索引构建完成，Hybrid Retrieval 可返回证据。
- [ ] M4：LangGraph 完整问答链路跑通，能输出英文 IRAC + Sources。
- [ ] M5：Citation Verification、RAGAS、自定义指标和 Langfuse 日志可展示。
- [ ] M6：Docker Compose 一键启动演示环境，README 可复现。
