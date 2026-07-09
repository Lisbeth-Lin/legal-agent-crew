# 16. Evaluation Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

实现 RAGAS 指标和法律场景自定义指标，形成可展示的质量评估闭环。

## 2. 前置依赖

Citation Verification, Logging。

## 3. 交付物

- EvaluationResult
- evaluation_logs

## 4. 最小任务 Checklist

- [ ] E-01 定义 EvaluationInput：question、answer、contexts、citations、ground_truth。
- [ ] E-02 定义 EvaluationResult：faithfulness、answer_relevance、context_precision、context_recall、citation_accuracy、paragraph_match_rate、source_grounding_rate、unsupported_claim_rate、fallback_trigger_accuracy、latency、token_usage。
- [ ] E-03 接入 RAGAS，计算 faithfulness、answer_relevance、context_precision、context_recall。
- [ ] E-04 实现 Citation Accuracy：有效引用数 / 总引用数。
- [ ] E-05 实现 Paragraph Match Rate：段落号正确引用数 / 带段落号引用数。
- [ ] E-06 实现 Unsupported Claim Rate：unsupported_claims 数量 / 关键 claim 数量。
- [ ] E-07 实现 Retrieval Hit Rate 的可选人工标注接口。
- [ ] E-08 将评测结果写入 evaluation_logs 表。
- [ ] E-09 提供 /evaluation/run API 调用入口。

## 5. 独立测试 Checklist

- [ ] TEST-01 无引用答案 citation_accuracy=0。
- [ ] TEST-02 全部引用通过校验 citation_accuracy=1。
- [ ] TEST-03 evaluation_logs 能保存完整指标 JSON。
- [ ] TEST-04 RAGAS 不可用时自定义指标仍可运行。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
