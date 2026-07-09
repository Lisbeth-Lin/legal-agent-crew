# 10. Query Rewrite Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

将用户问题改写为适合 BM25 和向量检索的关键词查询、语义查询和元数据过滤建议。

## 2. 前置依赖

Query Classifier, Config Management。

## 3. 交付物

- QueryRewriteResult

## 4. 最小任务 Checklist

- [ ] QR-01 定义 QueryRewriteResult：keyword_queries、semantic_queries、legal_terms、case_names、metadata_filters。
- [ ] QR-02 实现规则抽取：识别案例名、条约条文、Article 编号、常见国际法术语。
- [ ] QR-03 实现 LLM query rewrite prompt，要求输出英文检索查询。
- [ ] QR-04 对中文问题生成英文 semantic query 和关键法律术语。
- [ ] QR-05 为 case_comparison 类型分别生成每个案例的检索 query。
- [ ] QR-06 限制 rewrite 不添加用户问题中不存在的事实性限定。

## 5. 独立测试 Checklist

- [ ] TEST-01 中文“国家责任 attribution”问题能生成 attribution / state responsibility 查询。
- [ ] TEST-02 案例对比问题能拆成两个 case query。
- [ ] TEST-03 Article 31 VCLT 能被保留为关键词查询。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
