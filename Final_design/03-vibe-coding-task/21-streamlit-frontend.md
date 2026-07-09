# 21. Streamlit Frontend Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

保留 Streamlit 作为演示前端，通过 HTTP 调用 FastAPI，不承载核心业务逻辑。

## 2. 前置依赖

FastAPI Backend。

## 3. 交付物

- Streamlit 页面
- 前端 API client
- 演示 UI

## 4. 最小任务 Checklist

- [ ] SF-01 创建 frontend/app.py，配置 API_BASE_URL。
- [ ] SF-02 实现文档上传页：上传 PDF、填写元数据、调用 /documents/upload。
- [ ] SF-03 实现知识库管理页：展示文档列表、筛选、状态、重新解析、重新索引、删除。
- [ ] SF-04 实现问答页：输入问题、选择 legal_domain、是否启用联网补充、调用 /qa/ask。
- [ ] SF-05 实现 IRAC 答案展示区。
- [ ] SF-06 实现 Sources 引用卡片：标题、页码、段落号、原句。
- [ ] SF-07 实现案例检索页，调用 /retrieval/hybrid-search 或业务 API。
- [ ] SF-08 实现案例对比页，输入多个案例名和对比主题。
- [ ] SF-09 实现日志 / 评测展示区：trace_id、fallback 是否触发、latency、citation_accuracy。
- [ ] SF-10 移除或隔离原型中直接调用模型、Milvus、Firecrawl 的逻辑。

## 5. 独立测试 Checklist

- [ ] TEST-01 前端上传页能调用后端并展示 doc_id。
- [ ] TEST-02 问答页能展示 IRAC 和 Sources。
- [ ] TEST-03 后端错误能在前端清晰显示。
- [ ] TEST-04 Streamlit 不直接 import 核心服务层。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
