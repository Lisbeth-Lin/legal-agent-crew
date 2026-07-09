# 09. Query Classifier Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

识别用户问题类型，为后续 Legal Intent Router 和输出模板选择提供依据。

## 2. 前置依赖

Config Management, LLM Provider。

## 3. 交付物

- QueryClassificationResult

## 4. 最小任务 Checklist

- [ ] QC-01 定义 query_type 枚举：concept_explanation、case_search、case_summary、rule_analysis、treaty_interpretation、case_comparison、exam_answer、citation_lookup、unsupported_or_unclear。
- [ ] QC-02 实现 QueryClassifier.classify(question)。
- [ ] QC-03 优先实现规则分类 baseline：识别 compare、summarize、case、concept、Article 等关键词。
- [ ] QC-04 实现 LLM 分类 fallback，输出 JSON 并用 Pydantic 校验。
- [ ] QC-05 返回 confidence、query_type、reason。
- [ ] QC-06 分类失败时返回 unsupported_or_unclear，不抛出系统异常。

## 5. 独立测试 Checklist

- [ ] TEST-01 输入案例对比问题返回 case_comparison。
- [ ] TEST-02 输入概念问题返回 concept_explanation。
- [ ] TEST-03 LLM 输出非法 JSON 时能 fallback。
- [ ] TEST-04 每种 query_type 至少有一个测试样例。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
