# 23. Testing and Quality Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

建立单元测试、集成测试、端到端测试和最小评测样例，保证模块可独立测试。

## 2. 前置依赖

全部模块。

## 3. 交付物

- pytest 测试集
- fixtures
- 质量检查脚本

## 4. 最小任务 Checklist

- [ ] TQ-01 创建 tests/fixtures，加入最小测试 PDF、mock chunks、mock evidence pack、mock LLM 输出。
- [ ] TQ-02 为每个 service 编写单元测试。
- [ ] TQ-03 为数据库 Repository 编写 CRUD 测试。
- [ ] TQ-04 为 PDF Parsing 编写文本 PDF、无段落号 PDF、OCR fallback mock 测试。
- [ ] TQ-05 为 Hybrid Retrieval 编写 BM25/Dense/Rerank mock 集成测试。
- [ ] TQ-06 为 LangGraph workflow 编写 answerable、unanswerable、citation_failed 三条分支测试。
- [ ] TQ-07 为 FastAPI 编写 TestClient API 测试。
- [ ] TQ-08 创建最小评测集 evaluation/sample_questions.jsonl，包含 question、expected_source、ground_truth 可选字段。
- [ ] TQ-09 配置 ruff、mypy 或 pyright，至少保证核心模块类型检查。

## 5. 独立测试 Checklist

- [ ] TEST-01 pytest 全部通过。
- [ ] TEST-02 核心模块覆盖率达到可接受阈值。
- [ ] TEST-03 lint 和 type check 能通过。
- [ ] TEST-04 sample_questions 至少能跑通 5 条。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
