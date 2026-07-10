# 13. Trusted Web Search Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

将原型 Firecrawl fallback 升级为受来源白名单约束的可信联网补充工具。

## 2. 前置依赖

Config Management, Answerability Evaluator。

## 3. 交付物

- WebEvidenceResult

## 4. 最小任务 Checklist

- [ ] TWS-01 实现 TrustedSourcePolicy，从 sources.yaml 读取 trusted_domains、blocked_domains、source_priority。
- [ ] TWS-02 封装 FirecrawlSearchClient，输入 query 和 allowed_domains。
- [ ] TWS-03 实现 search_trusted_sources(query, filters)，默认只搜索白名单来源。
- [ ] TWS-04 为联网结果提取 title、url、snippet、source_type、trust_level。
- [ ] TWS-05 实现 Web Evidence Builder，将网页结果转换为 EvidenceChunk-like 结构。
- [ ] TWS-06 联网证据必须标记 source_origin=web，不得覆盖本地 PDF 优先级。
- [ ] TWS-07 记录 fallback_triggered、fallback_reason、web_sources 到日志表。

## 5. 独立测试 Checklist

- [ ] TEST-01 blocked domain 结果被过滤。
- [ ] TEST-02 白名单为空时不执行开放全网搜索。
- [ ] TEST-03 联网结果包含 URL、标题和摘要。
- [ ] TEST-04 fallback 日志能保存触发原因。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
