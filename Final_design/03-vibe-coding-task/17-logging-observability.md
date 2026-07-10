# 17. Logging and Observability Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

为每次问答生成 trace_id，记录检索、生成、引用校验、fallback、评测和错误信息。

## 2. 前置依赖

Database Models, Langfuse。

## 3. 交付物

- trace_logs
- error_logs
- Langfuse trace

## 4. 最小任务 Checklist

- [ ] LO-01 实现 TraceContext，生成 trace_id 并在 workflow state 中传递。
- [ ] LO-02 实现 LoggingService.log_event(trace_id, event_type, payload)。
- [ ] LO-03 记录 query classification、query rewrite、retrieval、rerank、answerability、web fallback、generation、citation verification、evaluation 事件。
- [ ] LO-04 实现 ErrorLoggingService，统一记录 module、error_type、message、stacktrace、trace_id。
- [ ] LO-05 接入 Langfuse client，记录关键 LLM span、retrieval span 和 workflow span。
- [ ] LO-06 当 Langfuse 配置缺失时降级为本地日志，不影响主流程。
- [ ] LO-07 提供 GET /qa/messages/{message_id} 时返回 trace_id 和基础日志摘要。

## 5. 独立测试 Checklist

- [ ] TEST-01 每次 /qa/ask 都生成 trace_id。
- [ ] TEST-02 检索和生成事件能写入 trace_logs。
- [ ] TEST-03 异常能写入 error_logs。
- [ ] TEST-04 Langfuse 不可用时主流程不崩溃。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
