# 06. Knowledge Base Management Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

提供已入库文档的查看、筛选、状态管理、重新解析、重新索引和删除能力。

## 2. 前置依赖

Database Models, PDF Parsing, Indexing。

## 3. 交付物

- 知识库服务
- 文档管理 API 支撑逻辑

## 4. 最小任务 Checklist

- [ ] KBM-01 实现 DocumentListQuery schema，支持 title、institution、year、legal_domain、document_type、parse_status、index_status 筛选。
- [ ] KBM-02 实现 list_documents 分页查询。
- [ ] KBM-03 实现 get_document_detail，返回文档元数据、页数、chunk 数、状态。
- [ ] KBM-04 实现 list_document_chunks，支持按页码和段落号筛选。
- [ ] KBM-05 实现 update_document_metadata。
- [ ] KBM-06 实现 reparse_document：清理旧 page/chunk/citation，再重新解析。
- [ ] KBM-07 实现 reindex_document：调用 Indexing Module 重建 BM25 与向量索引。
- [ ] KBM-08 实现 delete_document：删除原始文件、数据库记录、Milvus 向量、Elasticsearch 索引。

## 5. 独立测试 Checklist

- [ ] TEST-01 可按 legal_domain 和 institution 筛选文档。
- [ ] TEST-02 重新解析会替换旧 chunks。
- [ ] TEST-03 删除文档后业务库和索引库都无残留记录。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
