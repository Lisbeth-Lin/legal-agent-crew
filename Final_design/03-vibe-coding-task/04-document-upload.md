# 04. Document Upload Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

实现 PDF 上传、文件校验、重复检测、元数据入库和解析任务触发入口。

## 2. 前置依赖

Database Models, Config Management。

## 3. 交付物

- 上传服务
- 文件存储路径
- 文档元数据记录

## 4. 最小任务 Checklist

- [ ] DU-01 定义 DocumentUploadRequest / DocumentUploadResponse Pydantic schema。
- [ ] DU-02 实现 PDF 文件类型校验：扩展名、MIME type、文件大小。
- [ ] DU-03 实现文件 hash 计算，用于重复文件检测。
- [ ] DU-04 实现本地文件系统保存策略：data/raw/{doc_id}.pdf。
- [ ] DU-05 将文档级元数据写入 documents 表，初始 parse_status=not_parsed、index_status=not_indexed。
- [ ] DU-06 实现上传后可选自动触发解析的参数 auto_parse。
- [ ] DU-07 实现上传失败时清理临时文件和错误日志记录。

## 5. 独立测试 Checklist

- [ ] TEST-01 上传合法 PDF 后 documents 表生成记录。
- [ ] TEST-02 重复上传同一文件时返回明确提示。
- [ ] TEST-03 上传非 PDF 文件被拒绝。
- [ ] TEST-04 文件保存失败时数据库不残留脏记录。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
