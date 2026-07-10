# 15. Citation Verification Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

校验答案引用是否来自 Evidence Pack，并判断关键 claim 是否有原文支持。

## 2. 前置依赖

Legal Reasoning Generator, Evidence Pack Builder。

## 3. 交付物

- CitationVerificationResult

## 4. 最小任务 Checklist

- [ ] CV-01 定义 CitationVerificationInput：answer、citations、evidence_pack。
- [ ] CV-02 定义 CitationVerificationResult：status、unsupported_claims、invalid_citations、suggested_action。
- [ ] CV-03 实现引用存在性校验：答案中的 citation_anchor 必须存在于 evidence_pack。
- [ ] CV-04 实现页码和段落号校验：citation 中 page_number / paragraph_number 与 chunk metadata 一致。
- [ ] CV-05 实现原句支持校验 baseline：引用原句必须是 chunk text 子串或近似匹配。
- [ ] CV-06 实现 LLM claim support check：抽取关键 claim，判断是否被 evidence 支持。
- [ ] CV-07 当校验 failed 时返回 revise_answer 或 retrieve_more。
- [ ] CV-08 将有效引用写入 answer_citations 表。

## 5. 独立测试 Checklist

- [ ] TEST-01 虚构 citation_anchor 会被标记 invalid。
- [ ] TEST-02 错误页码会被标记 invalid。
- [ ] TEST-03 无证据支持的 claim 会出现在 unsupported_claims。
- [ ] TEST-04 通过校验的引用能写入 answer_citations。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
