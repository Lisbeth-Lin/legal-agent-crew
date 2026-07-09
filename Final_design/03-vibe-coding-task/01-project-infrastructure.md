# 01. Project Infrastructure Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

建立最终版项目的基础工程结构，使后续模块可以独立开发、测试和接入。

## 2. 前置依赖

无。

## 3. 交付物

- 统一目录结构
- 依赖管理文件
- 基础运行入口
- 开发脚本

## 4. 最小任务 Checklist

- [ ] PI-01 创建最终版工程目录：app/api、app/core、app/db、app/models、app/repositories、app/services、app/tools、app/workflows、frontend、tests、config、scripts。
- [ ] PI-02 整理原型代码，将 Streamlit 原型逻辑暂存到 legacy/ 或 frontend/legacy/，避免与最终后端逻辑耦合。
- [ ] PI-03 创建 pyproject.toml 或 requirements.txt，加入 FastAPI、uvicorn、pydantic、SQLAlchemy、alembic、pymupdf、pypdf、sentence-transformers、pymilvus、elasticsearch、langgraph、ragas、langfuse、streamlit 等依赖。
- [ ] PI-04 创建 .env.example，声明 DATABASE_URL、MILVUS_URI、ELASTICSEARCH_URL、LLM_API_KEY、LLM_BASE_URL、FIREFCRAWL_API_KEY、LANGFUSE_PUBLIC_KEY、LANGFUSE_SECRET_KEY 等变量。
- [ ] PI-05 创建 app/main.py，提供 FastAPI app 初始化和 /health 路由。
- [ ] PI-06 创建 Makefile 或 scripts/dev.sh，提供 install、run-api、run-frontend、test、lint、format 命令。
- [ ] PI-07 创建基础 README 片段，说明当前任务目录和模块开发顺序。

## 5. 独立测试 Checklist

- [ ] TEST-01 运行 API 服务后 GET /health 返回 ok。
- [ ] TEST-02 pytest 能发现 tests/ 目录且至少通过一个 smoke test。
- [ ] TEST-03 环境变量缺失时有清晰错误提示。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
