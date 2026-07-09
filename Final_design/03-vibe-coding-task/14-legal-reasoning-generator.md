# 14. Legal Reasoning Generator Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

基于 Evidence Pack 生成默认英文 IRAC + Sources 法律答案，禁止自由编造引用。

## 2. 前置依赖

Evidence Pack Builder, LLM Provider。

## 3. 交付物

- DraftAnswer
- IRAC answer

## 4. 最小任务 Checklist

- [ ] LRG-01 定义 LegalAnswer schema：issue、rule、application、conclusion、sources、follow_up_questions。
- [ ] LRG-02 实现 IRAC prompt，要求答案默认英文输出。
- [ ] LRG-03 将 Evidence Pack 以结构化 source block 传入模型。
- [ ] LRG-04 要求模型只引用 source block 中的 citation_anchor。
- [ ] LRG-05 为不同 query_type 设计输出模板分支：concept、case brief、comparison、rule analysis。
- [ ] LRG-06 实现模型输出 JSON / Markdown 的解析与校验。
- [ ] LRG-07 当证据不足时输出明确 limitation，不得生成确定结论。
- [ ] LRG-08 记录 model_runs：prompt、model、tokens、latency、raw_output。

## 5. 独立测试 Checklist

- [ ] TEST-01 生成答案包含 Issue/Rule/Application/Conclusion/Sources。
- [ ] TEST-02 Sources 中 citation_anchor 均来自 Evidence Pack。
- [ ] TEST-03 空证据时答案说明资料不足。
- [ ] TEST-04 中文问题默认仍输出英文答案。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
