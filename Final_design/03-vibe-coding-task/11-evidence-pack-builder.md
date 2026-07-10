# 11. Evidence Pack Builder Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

将重排后的 chunk 组织为可供生成器使用的 Evidence Pack，并控制 token、去重和来源优先级。

## 2. 前置依赖

Hybrid Retrieval。

## 3. 交付物

- EvidencePack

## 4. 最小任务 Checklist

- [ ] EPB-01 定义 EvidenceChunk schema：chunk_id、doc_id、title、page_number、paragraph_number、text、citation_anchor、scores。
- [ ] EPB-02 定义 EvidencePack schema：question、query_type、chunks、source_summary、token_count。
- [ ] EPB-03 实现同一文档相邻 chunk 合并策略，避免证据割裂。
- [ ] EPB-04 实现 evidence 去重：重复文本、相同 citation_anchor、同一段落重复结果。
- [ ] EPB-05 实现 token budget 控制，超出预算时按 rerank_score 和来源优先级裁剪。
- [ ] EPB-06 优先保留官方案例 PDF，联网证据仅在本地不足时加入。
- [ ] EPB-07 为每个 evidence 生成前端可展示的 citation card 数据。

## 5. 独立测试 Checklist

- [ ] TEST-01 重复 chunk 会被去重。
- [ ] TEST-02 超出 token budget 时保留高分 evidence。
- [ ] TEST-03 Evidence Pack 中每个 chunk 都有 citation_anchor。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
