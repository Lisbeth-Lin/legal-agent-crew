# 24. Docker Deployment Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

用 Docker Compose 管理 FastAPI、Streamlit、PostgreSQL、Milvus、Elasticsearch、Redis 等服务。

## 2. 前置依赖

Project Infrastructure, Config Management。

## 3. 交付物

- Dockerfile
- docker-compose.yml
- 部署说明

## 4. 最小任务 Checklist

- [ ] DD-01 为 FastAPI 创建 Dockerfile。
- [ ] DD-02 为 Streamlit 创建 Dockerfile 或复用同一镜像不同启动命令。
- [ ] DD-03 创建 docker-compose.yml，包含 api、frontend、postgres、milvus、elasticsearch、redis 可选服务。
- [ ] DD-04 配置 PostgreSQL volume、Milvus volume、Elasticsearch volume。
- [ ] DD-05 配置服务健康检查和 depends_on。
- [ ] DD-06 创建 scripts/init_db.sh，运行 Alembic migration。
- [ ] DD-07 创建 scripts/start_demo.sh，一键启动最终演示环境。
- [ ] DD-08 在 README 中记录本地启动步骤和常见问题。

## 5. 独立测试 Checklist

- [ ] TEST-01 docker compose config 校验通过。
- [ ] TEST-02 docker compose up 后 /health 可访问。
- [ ] TEST-03 PostgreSQL 和 Milvus 数据 volume 持久化。
- [ ] TEST-04 关闭外部 API key 时系统能启动但相关功能给出配置提示。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
