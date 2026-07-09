# 19. MCP-style Tools Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

将 PDF 解析、本地检索、联网检索、引用校验和评测能力封装为标准化工具接口。

## 2. 前置依赖

各 Service 模块。

## 3. 交付物

- Tool base class
- 工具输入输出 schema
- 工具注册表

## 4. 最小任务 Checklist

- [ ] MST-01 定义 BaseTool：name、description、input_schema、output_schema、run。
- [ ] MST-02 实现 PDFParserTool，封装 PDFParsingService。
- [ ] MST-03 实现 LocalKnowledgeBaseTool，封装文档和 chunk 查询能力。
- [ ] MST-04 实现 HybridRetrievalTool，封装 HybridRetrievalService。
- [ ] MST-05 实现 TrustedWebSearchTool，封装 TrustedWebSearchService。
- [ ] MST-06 实现 CitationVerificationTool，封装 CitationVerificationService。
- [ ] MST-07 实现 EvaluationTool，封装 EvaluationService。
- [ ] MST-08 实现 LoggingTool，封装 LoggingService。
- [ ] MST-09 实现 ToolRegistry，按 name 获取工具，便于后续升级为真正 MCP Server。

## 5. 独立测试 Checklist

- [ ] TEST-01 每个工具能用 Pydantic 校验输入输出。
- [ ] TEST-02 ToolRegistry 能按名称返回工具。
- [ ] TEST-03 工具内部异常会转换为统一 ToolError。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
