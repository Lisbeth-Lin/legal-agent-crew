# 03. Database Models Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

建立 PostgreSQL 业务主库模型，保存文档、chunk、引用、问答、日志和评测数据。

## 2. 前置依赖

Project Infrastructure, Config Management。

## 3. 交付物

- SQLAlchemy models
- Alembic migrations
- Repository 层

## 4. 最小任务 Checklist

- [ ] DM-01 创建数据库连接模块 app/db/session.py，支持同步或异步 Session，优先保持实现简单。
- [ ] DM-02 创建 Alembic 初始化配置。
- [ ] DM-03 实现 documents 表模型：doc_id、title、institution、year、legal_domain、document_type、language、source_url、file_path、parse_status、index_status、upload_time。
- [ ] DM-04 实现 document_pages 表模型：page_id、doc_id、page_number、text、parse_method、ocr_used。
- [ ] DM-05 实现 document_chunks 表模型：chunk_id、doc_id、page_number、paragraph_number、section_title、text、citation_anchor、embedding_id、bm25_id。
- [ ] DM-06 实现 citation_anchors 表模型：citation_id、chunk_id、doc_id、title、page_number、paragraph_number、original_sentence、citation_text。
- [ ] DM-07 实现 qa_sessions、qa_messages、retrieval_results、answer_citations、model_runs、trace_logs、evaluation_logs、error_logs 表模型。
- [ ] DM-08 为每张表实现最小 Repository：create、get_by_id、list、update_status、delete。
- [ ] DM-09 生成首个 Alembic migration。

## 5. 独立测试 Checklist

- [ ] TEST-01 使用测试数据库创建所有表成功。
- [ ] TEST-02 documents 与 document_chunks 的外键关系正确。
- [ ] TEST-03 Repository create/get/list/update/delete 单元测试通过。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
