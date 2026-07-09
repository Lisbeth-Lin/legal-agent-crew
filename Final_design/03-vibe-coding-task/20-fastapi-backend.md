# 20. FastAPI Backend Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

提供文档、问答、检索、引用和评测 API，承接 Streamlit 前端调用。

## 2. 前置依赖

所有核心 Service 模块。

## 3. 交付物

- FastAPI routers
- API schemas
- 统一错误响应

## 4. 最小任务 Checklist

- [ ] FB-01 创建 app/api/documents.py，实现 POST /documents/upload。
- [ ] FB-02 实现 GET /documents、GET /documents/{doc_id}。
- [ ] FB-03 实现 POST /documents/{doc_id}/parse、POST /documents/{doc_id}/index。
- [ ] FB-04 实现 DELETE /documents/{doc_id}。
- [ ] FB-05 创建 app/api/qa.py，实现 POST /qa/ask、GET /qa/sessions、GET /qa/sessions/{session_id}、GET /qa/messages/{message_id}。
- [ ] FB-06 创建 app/api/retrieval.py，实现 POST /retrieval/search、POST /retrieval/hybrid-search、POST /retrieval/rerank。
- [ ] FB-07 创建 app/api/citations.py，实现 GET /citations/{citation_id}、POST /citations/verify。
- [ ] FB-08 创建 app/api/evaluation.py，实现 POST /evaluation/run、GET /evaluation/runs、GET /evaluation/runs/{run_id}。
- [ ] FB-09 实现统一错误响应格式：code、message、detail、trace_id。
- [ ] FB-10 实现 CORS 配置，支持 Streamlit 本地访问。

## 5. 独立测试 Checklist

- [ ] TEST-01 所有 API OpenAPI schema 可生成。
- [ ] TEST-02 /documents/upload 可上传测试 PDF。
- [ ] TEST-03 /qa/ask 返回 final_answer、sources、trace_id。
- [ ] TEST-04 错误场景返回统一错误格式。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
