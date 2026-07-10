# 07. Indexing Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

为 document_chunks 构建 Milvus dense vector 索引和 Elasticsearch BM25 索引。

## 2. 前置依赖

PDF Parsing, Config Management。

## 3. 交付物

- Embedding 服务
- Milvus collection
- Elasticsearch index
- 索引状态

## 4. 最小任务 Checklist

- [ ] I-01 实现 EmbeddingProvider，加载 BAAI/bge-m3，提供 embed_texts(texts)。
- [ ] I-02 实现 MilvusClient 封装：connect、create_collection、upsert_chunks、delete_by_doc_id、search。
- [ ] I-03 将原型 binary vector 主方案替换为 FLOAT_VECTOR，默认 cosine 或 inner product。
- [ ] I-04 实现 ElasticsearchClient 封装：create_index、upsert_chunks、delete_by_doc_id、bm25_search。
- [ ] I-05 设计 Elasticsearch mapping，包含 text、title、institution、legal_domain、document_type、page_number、paragraph_number。
- [ ] I-06 实现 IndexingService.index_document(doc_id)，读取 chunks，批量 embedding，写入 Milvus 和 Elasticsearch。
- [ ] I-07 将 Milvus embedding_id 和 Elasticsearch bm25_id 回写 document_chunks。
- [ ] I-08 更新 documents.index_status 为 indexed / failed。
- [ ] I-09 实现批量重建索引脚本 scripts/reindex_all.py。

## 5. 独立测试 Checklist

- [ ] TEST-01 单个文档 index 后 index_status=indexed。
- [ ] TEST-02 Milvus 能按向量返回 chunk_id。
- [ ] TEST-03 Elasticsearch 能按案例名或术语返回 chunk_id。
- [ ] TEST-04 索引失败时不影响原始解析数据。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
