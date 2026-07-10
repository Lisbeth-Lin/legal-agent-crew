# 12. Answerability Evaluator Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

判断本地 Evidence Pack 是否足以回答问题，并决定是否触发可信联网补充。

## 2. 前置依赖

Evidence Pack Builder, LLM Provider。

## 3. 交付物

- AnswerabilityResult

## 4. 最小任务 Checklist

- [ ] AE-01 定义 AnswerabilityResult：answerability、source_sufficiency、citation_confidence、needs_web_fallback、reason。
- [ ] AE-02 实现规则 baseline：evidence 数量不足、rerank_score 过低、来源不匹配时判定 partially_answerable。
- [ ] AE-03 实现 LLM evaluator，基于 question + evidence summaries 输出结构化 JSON。
- [ ] AE-04 设置阈值：source_sufficiency < threshold 时触发 fallback。
- [ ] AE-05 记录触发 fallback 的原因，用于 Fallback Trigger Accuracy。
- [ ] AE-06 避免 evaluator 基于模型内部知识判断“可回答”，只能依据 evidence。

## 5. 独立测试 Checklist

- [ ] TEST-01 空 Evidence Pack 返回 unanswerable 且 needs_web_fallback=true。
- [ ] TEST-02 高相关 evidence 返回 answerable。
- [ ] TEST-03 低分 evidence 返回 partially_answerable。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
