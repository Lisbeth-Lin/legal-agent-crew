# 08. Hybrid Retrieval Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

实现 BM25 + Dense Retrieval + Metadata Filter + RRF/加权融合 + Reranker 的证据召回链路。

## 2. 前置依赖

Indexing, Config Management。

## 3. 交付物

- HybridRetrievalService
- RetrievalResult
- 候选 evidence

## 4. 最小任务 Checklist

- [ ] HR-01 定义 RetrievalRequest schema：query、keyword_query、semantic_query、legal_domain、institution、document_type、year_range、top_k。
- [ ] HR-02 实现 BM25 检索调用 Elasticsearch，返回 bm25_score 和 chunk metadata。
- [ ] HR-03 实现 Dense 检索调用 Milvus，返回 dense_score 和 chunk metadata。
- [ ] HR-04 实现 metadata filter，确保 BM25 与 Dense 使用相同过滤条件。
- [ ] HR-05 实现候选结果去重，按 chunk_id 合并分数。
- [ ] HR-06 实现 RRF 融合策略，支持从 retrieval.yaml 配置 rrf_k。
- [ ] HR-07 实现 bge-reranker-v2-m3 重排，输入 query + chunk text，输出 rerank_score。
- [ ] HR-08 输出 top rerank_k 作为 Evidence Candidate。
- [ ] HR-09 将检索过程写入 retrieval_results 表。

## 5. 独立测试 Checklist

- [ ] TEST-01 BM25 与 Dense 结果能合并去重。
- [ ] TEST-02 metadata filter 能限制 legal_domain。
- [ ] TEST-03 reranker 后排序稳定返回 top_k。
- [ ] TEST-04 检索结果能写入 retrieval_results。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
