# 02. Config Management Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

用 YAML + .env 管理模型、检索、来源、prompt 和评测参数，避免硬编码。

## 2. 前置依赖

Project Infrastructure。

## 3. 交付物

- config/*.yaml
- 配置加载器
- 配置 schema

## 4. 最小任务 Checklist

- [ ] CM-01 创建 config/sources.yaml，定义 trusted_domains、source_priority、blocked_domains、institution_mapping。
- [ ] CM-02 创建 config/models.yaml，定义 llm provider、embedding model、reranker model、temperature、max_tokens。
- [ ] CM-03 创建 config/retrieval.yaml，定义 bm25_top_k、dense_top_k、rerank_top_k、rrf_k、score_threshold、metadata_filters。
- [ ] CM-04 创建 config/prompts.yaml，定义 query_classifier、query_rewrite、answerability、legal_reasoning、citation_verifier prompt。
- [ ] CM-05 创建 config/evaluation.yaml，定义 RAGAS 指标和自定义 citation 指标开关。
- [ ] CM-06 实现 app/core/config.py，加载 .env 与 YAML，并用 Pydantic 校验。
- [ ] CM-07 实现配置热加载或重启加载策略，至少支持单元测试中替换测试配置。

## 5. 独立测试 Checklist

- [ ] TEST-01 缺少必要配置时抛出 ConfigError。
- [ ] TEST-02 测试配置能覆盖默认配置。
- [ ] TEST-03 retrieval.yaml 中 top_k 参数能被 Hybrid Retrieval 读取。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
