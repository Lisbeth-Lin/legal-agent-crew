# Proposal：Agentic RAG 国际公法研究助手（最终版 v3）

> 项目名称：**Agentic RAG 国际公法研究助手**
> 英文代号：**PublicLaw Research Agent**
> 文档类型：需求文档 / Proposal
> 项目用途：简历项目展示 / 大模型 Agent 应用项目
> 版本定位：在现有国际公法问答 Agent 原型基础上的最终版需求文档
> 前端形态：**FastAPI 后端 + Streamlit 演示前端**
> 默认回答语言：**English**
> 默认回答格式：**IRAC + Sources**

---

## 1. 项目背景

国际公法学习和研究高度依赖权威法律资料，包括国际法院判决、WTO 专家组 / 上诉机构报告、投资仲裁裁决、国际海洋法案件、条约文本、国际组织文件、权威教材和学术论文等。传统检索方式需要人工阅读大量 PDF，效率较低；通用大模型虽然能够生成类似法律分析的回答，但存在来源不可控、引用不稳定、段落定位不精确、容易幻觉、难以评估等问题。

本项目拟在现有法律 PDF 问答 Agent 原型的基础上，构建一个面向国际公法场景的 **Agentic RAG 法律研究助手**。系统以提前爬取并整理好的国际公法案例 PDF 为主要知识基础，通过结构化 PDF 解析、段落级切分、混合检索、引用锚点、MCP-style 工具层、IRAC 法律推理生成、引用校验、可信联网补充和评测日志，帮助用户获得有权威来源、可追溯、可验证、可评估的英文法律问答结果。

本项目的核心不是简单调用大模型 API，而是将大模型作为推理与编排引擎，将权威法律资料、检索系统、引用验证、联网补充、评测指标和日志记录纳入统一控制流程，从而降低法律问答中的幻觉风险，提高答案的来源可靠性和工程可解释性。

---

## 2. 项目定位

### 2.1 一句话定位

**Agentic RAG 国际公法研究助手是一个基于国际公法案例 PDF 和权威法律资料的可溯源英文问答系统，支持 IRAC 法律分析、段落级引用、案例检索、案例摘要、概念解释、案例对比、联网补充、引用校验和质量评估。**

### 2.2 与通用大模型的区别

| 维度 | 通用大模型 | 本系统 |
|---|---|---|
| 知识来源 | 模型内部知识，来源不可控 | 预先爬取的国际公法案例 PDF + 指定权威网址 / 教材 / 学术论文 |
| 引用能力 | 可能编造或引用不精确 | 文档标题 + 页码 + 段落号 / 原句 |
| 回答结构 | 泛化回答 | 默认英文 IRAC + Sources |
| 检索能力 | 不透明 | Elasticsearch BM25 + Milvus 向量检索 + Reranker + Metadata Filter |
| 工具能力 | 依赖模型自身 | MCP-style 工具层统一封装 PDF 解析、官方资料检索、Citation 验证和评测工具 |
| 可靠性 | 难以评估 | 基础日志 + Langfuse Trace + RAGAS + Citation Accuracy + Fallback Trigger Accuracy |
| 法律适配 | 不区分任务类型 | 支持概念解释、案例检索、case brief、案例对比、条约 / 案例规则分析 |

---

## 3. 原型现状与最终版升级目标

### 3.1 当前原型技术栈

当前仓库中的原型更接近于一个法律 PDF Agentic RAG demo，主要技术栈为：

```text
Streamlit
+ CrewAI Flow
+ pypdf
+ sentence-transformers / BAAI/bge-large-en-v1.5
+ numpy binary quantization
+ Milvus Lite BINARY_VECTOR
+ Hamming Distance
+ LLM-as-Judge
+ Firecrawl Web Search fallback
+ Qwen / OpenAI-compatible API
+ Pydantic
```

当前原型已经具备以下基础能力：

1. 通过 Streamlit 提供简单问答界面。
2. 支持上传法律 PDF 并进行基础文本解析。
3. 使用 Embedding + Milvus Lite 进行本地向量检索。
4. 使用 RAG 方式基于 PDF chunk 生成答案。
5. 使用 LLM-as-Judge 判断回答质量。
6. 在本地证据不足时调用 Firecrawl 进行 Web Search fallback。

### 3.2 当前原型的主要不足

1. **缺少 FastAPI 后端服务层**：业务逻辑与前端耦合，不利于后续扩展 API、测试和部署。
2. **PDF 解析不够法律结构感知**：仅依赖 pypdf 难以稳定保留页码、段落号、章节标题和原句。
3. **检索链路偏单一**：主要依赖向量检索，缺少 BM25 对案件名称、条约条文和法律术语的精确匹配。
4. **Embedding 选型不够适配跨语言场景**：bge-large-en-v1.5 更偏英文语义检索，难以充分支持中文问题与英文材料之间的跨语言匹配。
5. **Binary Vector 不适合作为最终主检索方案**：二值量化节省存储，但可能损失法律段落检索所需的细粒度语义信息。
6. **缺少 Reranker**：无法对 BM25 与向量召回后的候选证据进行高精度重排。
7. **缺少业务数据库层**：文档元数据、chunk、引用锚点、问答日志和评测记录没有统一管理。
8. **Citation Verification 不完整**：当前 citation snippet 展示不足以保证答案关键 claim 与来源一一对应。
9. **缺少完整评测闭环**：尚未系统接入 RAGAS、Citation Accuracy、Fallback Trigger Accuracy 等指标。
10. **可观测性不足**：缺少面向检索、生成、引用校验和 fallback 的 trace 记录。

### 3.3 最终版升级目标

最终版应从“可运行 demo”升级为“可检索、可引用、可校验、可评估、可展示的国际公法 Agentic RAG 系统”。最终技术栈目标为：

```text
FastAPI + Streamlit
LangGraph + Pydantic
PyMuPDF + pypdf + Unstructured
PaddleOCR
PostgreSQL + SQLAlchemy + Alembic
Milvus Lite / Milvus Standalone
Elasticsearch BM25
BAAI/bge-m3
BAAI/bge-reranker-v2-m3
Firecrawl + Trusted Source Whitelist
RAGAS + Custom Citation Metrics
Langfuse
Docker Compose
YAML + .env
```

---

## 4. 系统名称

### 4.1 推荐名称

**Agentic RAG 国际公法研究助手**

### 4.2 英文代号

**PublicLaw Research Agent**

### 4.3 命名理由

1. **Agentic RAG** 突出项目不是普通 RAG，而是包含查询分类、证据检索、回答可答性判断、联网补充、引用校验和评测日志的智能工作流。
2. **国际公法研究助手** 明确系统服务场景是国际公法学习、研究和案例分析。
3. **PublicLaw Research Agent** 便于在简历、GitHub README 和面试中作为英文项目名展示。

---

## 5. 项目目标

### 5.1 总体目标

构建一个面向国际公法场景的英文智能问答系统，使用户能够基于已入库的国际公法案例 PDF 和指定权威资料，获得结构化、可引用、可追溯、可校验、可评估的法律分析答案。

### 5.2 具体目标

1. 支持国际公法案例 PDF 的上传、解析、切分、入库和索引构建。
2. 支持将提前爬取好的案例 PDF 存入数据库，并形成可检索知识库。
3. 支持基于 RAG 的英文法律问答，默认输出 IRAC 结构。
4. 支持答案自动附带引用来源，引用精确到文档标题、页码、段落号或原句。
5. 支持案例检索与案例摘要，生成结构化 case brief。
6. 支持国际公法概念解释，结合案例、条约、教材或论文来源进行说明。
7. 支持两个或多个案例的对比分析。
8. 支持在本地知识库不足时联网查询指定优先参考渠道。
9. 支持 MCP-style 工具层，将官方资料检索、PDF 解析、Citation 验证、评测工具标准化接入。
10. 支持基础评估日志，记录检索、生成、引用、联网 fallback 和评测结果。
11. 支持 RAGAS、Citation Accuracy、Paragraph Match Rate、Fallback Trigger Accuracy 等评测指标。
12. 支持 Langfuse 记录关键 Agentic RAG 节点的 trace、latency、token usage 和错误信息。
13. 形成一个适合简历展示和面试讲解的大模型 Agent 应用项目。

---

## 6. 系统范围

### 6.1 本版本包含的功能

本需求文档面向最终版本，包含以下功能：

1. PDF 上传与解析
2. 国际公法知识库管理
3. 基于 RAG 的英文问答
4. 答案自动引用来源
5. 案例检索与案例摘要
6. 法律概念解释
7. 案例对比
8. 联网补充检索
9. MCP-style 工具层
10. Agentic RAG 工作流
11. Citation Verification
12. 基础评估日志
13. RAGAS 与自定义评测指标
14. Langfuse 可观测性
15. FastAPI 后端与 Streamlit 前端

### 6.2 本版本不包含的内容

1. 不区分复杂用户角色和权限体系。
2. 不做商业级法律数据库。
3. 不训练本地法律大模型。
4. 不默认开放全网搜索，联网检索应优先使用用户指定的权威渠道。
5. 不将大模型内部知识作为最终法律依据。
6. 不将回答流畅度置于引用准确性和答案忠实度之上。
7. 不将 Streamlit 作为核心业务逻辑层，Streamlit 仅作为演示前端。
8. 不将 Milvus 作为业务数据库，Milvus 仅作为向量索引服务。
9. 不将 Elasticsearch 作为业务数据库，Elasticsearch 仅作为关键词全文检索服务。
10. 不使用模型自由生成 citation，所有 citation 必须来自 evidence pack 或 trusted web evidence。
11. 不在最终版中仅依赖向量检索，必须保留 BM25 关键词检索。
12. 不把 LLM-as-Judge 作为唯一评测方式，必须保留可计算指标。

---

## 7. 数据来源需求

### 7.1 本地 RAG 数据来源

RAG 的主要知识来源为用户提前爬取好的国际公法案例 PDF。这些 PDF 可以存入数据库，并经过解析、切分、向量化和索引构建后供系统检索。

建议支持的案例 PDF 类型包括：

1. ICJ 判决与咨询意见
2. WTO Panel Reports
3. WTO Appellate Body Reports
4. ICSID 投资仲裁裁决
5. ITLOS 国际海洋法案件
6. PCA 仲裁案件
7. UN 相关国际法文件
8. 其他用户提前整理的国际公法案例 PDF

### 7.2 联网补充数据来源

当本地知识库无法提供充分依据时，系统允许联网查询。联网查询应优先参考用户提供的权威网址渠道、权威教材和学术论文来源。

推荐支持以下来源类型：

1. 国际法院 / 国际组织官网
2. 条约数据库
3. 国际法相关官方文件库
4. 权威教材资料
5. 学术论文数据库或用户指定论文来源
6. 用户手动配置的优先参考网址

联网补充应使用 `sources.yaml` 配置可信来源白名单和可信等级，避免将普通网页作为高可信法律依据。

### 7.3 数据入库要求

每份 PDF 入库时应保存以下文档级元数据：

```json
{
  "doc_id": "string",
  "title": "string",
  "institution": "string",
  "year": "number | null",
  "legal_domain": "string",
  "document_type": "case_report | treaty | teaching_material | article | other",
  "language": "string",
  "source_url": "string | null",
  "file_path": "string",
  "upload_time": "datetime",
  "parse_status": "success | partial_success | failed",
  "index_status": "indexed | not_indexed | failed"
}
```

每个 chunk 应保存以下 chunk 级元数据：

```json
{
  "chunk_id": "string",
  "doc_id": "string",
  "title": "string",
  "page_number": "number | null",
  "paragraph_number": "string | null",
  "section_title": "string | null",
  "text": "string",
  "original_sentence": "string | null",
  "citation_anchor": "string",
  "embedding_id": "string | null",
  "bm25_id": "string | null"
}
```

---

## 8. 核心功能需求

## 8.1 PDF 上传与解析

### 功能说明

系统应支持上传国际公法相关 PDF，并将其转换为可检索、可引用、可向量化的结构化文本。

### 输入

1. PDF 文件
2. 文档标题
3. 机构 / 来源
4. 年份
5. 法律领域
6. 文档类型
7. 语言
8. 来源 URL
9. 课程或主题标签

### 技术设计

1. 主解析器使用 **PyMuPDF**，负责抽取文本、页码、block、line、span、页面结构和可能的坐标信息。
2. **pypdf** 作为辅助工具，用于读取 PDF 元数据、页数、拆分、合并和简单 PDF 操作。
3. 对复杂版式或 PyMuPDF 解析失败的文档，使用 **Unstructured** 作为兜底解析方案。
4. 对文本为空、乱码、字符过少或扫描页，调用 **PaddleOCR** 进行 OCR 兜底。
5. 解析结果应统一转为 `DocumentPage`、`DocumentChunk` 和 `CitationAnchor` 数据结构。

### 处理流程

1. 校验 PDF 文件格式、大小和重复性。
2. 使用 PyMuPDF 抽取 PDF 文本、页码、标题、脚注和段落结构。
3. 对扫描页启用 PaddleOCR 兜底解析。
4. 识别段落编号，例如 `para. 12`、`[12]`、`Article 31` 等。
5. 优先按法律语义边界切分文本，包括标题、段落号、条文号和判决 reasoning 边界。
6. 为每个 chunk 生成 citation anchor。
7. 将文档级元数据、页级文本、chunk 级文本和 citation anchor 写入 PostgreSQL。
8. 触发 Elasticsearch BM25 索引构建。
9. 触发 BGE-M3 embedding 生成和 Milvus 向量索引构建。
10. 记录解析状态和错误日志。

### 输出

1. 结构化文档记录
2. 页级文本
3. 段落级文本 chunk
4. 引用锚点
5. 解析状态
6. 解析错误日志

### 验收标准

1. 系统能够成功解析普通文本型 PDF。
2. 系统能够保留页码信息。
3. 系统能够尽量识别段落号或条文编号。
4. 每个 chunk 至少包含文档标题、页码和原文片段。
5. 解析失败时应记录错误原因。
6. 扫描页应通过 OCR 兜底生成可检索文本，并标记 `source_type = ocr`。

---

## 8.2 国际公法知识库管理

### 功能说明

系统应支持对已入库 PDF 进行统一管理，包括文档查看、分类、标签、解析状态、索引状态和重新索引。

### 功能需求

1. 查看所有入库文档。
2. 按标题、机构、年份、法律领域、文档类型筛选。
3. 查看每份文档的解析状态和索引状态。
4. 查看文档 chunk 切分结果。
5. 查看 citation anchor 结果。
6. 支持重新触发解析。
7. 支持重新构建 Elasticsearch BM25 索引。
8. 支持重新构建 Milvus 向量索引。
9. 支持删除文档及其索引。
10. 支持修改文档元数据。

### 推荐法律领域标签

1. General International Law
2. Law of Treaties
3. State Responsibility
4. International Dispute Settlement
5. WTO Law
6. International Investment Law
7. International Human Rights Law
8. International Criminal Law
9. Law of the Sea
10. Use of Force and International Security
11. Diplomatic and Consular Relations
12. International Environmental Law

### 验收标准

1. 系统能够展示文档列表和状态。
2. 系统能够按元数据筛选文档。
3. 系统能够查看 chunk 结果。
4. 系统能够查看 citation anchor。
5. 系统能够重新解析或重新索引单份文档。

---

## 8.3 基于 RAG 的英文问答

### 功能说明

系统应基于本地国际公法知识库进行英文问答。用户输入自然语言问题后，系统检索相关案例 PDF 或其他权威材料，并生成 IRAC 格式的英文答案。

### 输入

1. 用户英文或中文自然语言问题
2. 可选法律领域
3. 可选机构 / 文档类型 / 年份
4. 可选是否启用联网补充
5. 默认回答格式：英文 IRAC + Sources

### 技术设计

1. 使用 **LangGraph** 编排 Agentic RAG 工作流。
2. 使用 **BAAI/bge-m3** 生成 dense embedding，支持中文问题与英文法律资料之间的跨语言检索。
3. 使用 **Elasticsearch BM25** 进行法律术语、案例名称、条约条文和段落号的关键词检索。
4. 使用 **Milvus** 进行 dense vector retrieval。
5. 使用 **RRF 或 weighted fusion** 融合 BM25 与向量召回结果。
6. 使用 **BAAI/bge-reranker-v2-m3** 对候选 chunk 重排。
7. 使用 Answerability Evaluator 判断本地证据是否足够。
8. 使用 Citation Verifier 校验答案引用是否来自 evidence pack。

### 处理流程

1. 接收用户问题。
2. 识别问题类型，例如概念解释、案例检索、规则分析、案例对比、考试答题等。
3. 对问题进行 query rewrite，生成关键词查询和语义查询。
4. 使用 Elasticsearch BM25 进行关键词检索。
5. 使用 Milvus + BGE-M3 进行语义召回。
6. 使用 metadata filter 按机构、年份、法律领域、文档类型过滤。
7. 使用 fusion 策略合并 BM25 与向量召回结果。
8. 使用 bge-reranker-v2-m3 对候选 chunk 排序。
9. 构建 Evidence Pack。
10. 判断本地证据是否足够。
11. 若证据足够，生成英文 IRAC 答案。
12. 若证据不足，调用 Trusted Web Search Tool。
13. 对答案引用进行校验。
14. 返回最终答案、引用来源和可继续追问的问题。
15. 将检索、生成、引用和评测日志写入 PostgreSQL，并将 trace 写入 Langfuse。

### 默认输出结构

```text
Issue
Rule
Application
Conclusion
Sources
Follow-up Questions
```

### 验收标准

1. 系统能够基于本地知识库回答国际公法问题。
2. 系统默认输出英文答案。
3. 系统默认使用 IRAC 结构。
4. 答案必须附带引用来源。
5. 证据不足时不得编造结论，应说明当前知识库未检索到充分依据。
6. 每次问答应生成 trace ID。

---

## 8.4 答案自动引用来源

### 功能说明

系统应在答案中自动附上来源，使每个关键法律结论尽量对应具体文档、页码、段落号或原句。

### 引用粒度

系统引用应至少支持：

1. 文档标题
2. 页码
3. 段落号
4. 原句 / 原文片段

推荐引用格式：

```text
[Source: Appellate Body Report, US — Shrimp, p. 45, para. 121: "..."]
```

若文档没有段落号，则使用：

```text
[Source: Document Title, p. 12: "original sentence..."]
```

### 处理流程

1. PDF 入库阶段生成 citation anchor。
2. 检索阶段返回 chunk 及其 citation anchor。
3. 回答生成阶段要求模型仅引用 Evidence Pack 中的来源。
4. 回答生成后进行 citation verification。
5. 对虚构引用、错误页码、错误段落号进行拦截或标记。
6. 若 Citation Verifier 返回 `failed`，系统应触发答案修订或重新检索。
7. 前端展示引用卡片，支持查看原文片段。

### 验收标准

1. 答案中的引用必须来自本次检索上下文或联网工具返回结果。
2. 不允许模型自由生成不存在的引用。
3. 每条引用至少包含文档标题、页码和原文片段。
4. 如果段落号可识别，应优先展示段落号。
5. Citation Verifier 应记录 invalid citations 和 unsupported claims。

---

## 8.5 案例检索与案例摘要

### 功能说明

系统应支持根据案件名称、关键词、法律领域或问题检索国际公法案例，并生成适合法学学习和研究使用的结构化 case brief。

### 输入

1. 案件名称
2. 关键词
3. 法律领域
4. 机构
5. 年份
6. 文档类型

### 输出模板

```text
Case Name:
Institution:
Year:
Legal Field:
Core Facts:
Legal Issues:
Applicable Law:
Reasoning:
Holding / Conclusion:
Key Paragraphs:
Teaching Value:
Further Discussion Questions:
Sources:
```

### 验收标准

1. 系统能够返回相关案例列表。
2. 系统能够区分同名或相似案件。
3. 系统能够生成结构化英文 case brief。
4. 关键事实、争议问题、推理和结论应尽量附带来源。

---

## 8.6 法律概念解释

### 功能说明

系统应支持解释国际公法核心概念、条约术语、判例规则和学说争议，并结合案例、条约、教材或论文来源进行说明。

### 示例概念

1. jus cogens
2. opinio juris
3. erga omnes
4. effective control test
5. due diligence
6. necessity
7. countermeasures
8. self-defence
9. proportionality
10. national treatment
11. most-favoured-nation treatment
12. necessity test

### 输出模板

```text
Concept:
One-sentence Explanation:
Detailed Explanation:
Legal Sources:
Leading Cases:
Distinction from Similar Concepts:
Common Misunderstandings:
Exam / Research Usage:
Sources:
```

### 验收标准

1. 系统能够给出英文概念解释。
2. 系统能够结合来源材料，而不是百科式空泛解释。
3. 对争议性概念，应说明主流观点与争议点。
4. 对相近概念，应给出区别说明。

---

## 8.7 案例对比

### 功能说明

系统应支持比较两个或多个国际公法案例在事实、法律问题、适用规则、推理路径、结论和后续影响上的异同。

### 输入

1. 两个或多个案例名称
2. 对比主题
3. 输出格式：表格 / 文字分析 / 论文论证版

### 输出模板

| Comparison Dimension | Case A | Case B | Explanation |
|---|---|---|---|
| Facts |  |  |  |
| Legal Issues |  |  |  |
| Applicable Rules |  |  |  |
| Reasoning |  |  |  |
| Conclusion |  |  |  |
| Subsequent Influence |  |  |  |

### 验收标准

1. 系统能够识别待比较案例。
2. 系统能够分别检索每个案例的相关段落。
3. 系统能够按维度生成对比表。
4. 系统能够说明制度背景差异，例如 ICJ 与 WTO 的制度差异。
5. 对比结论应附带来源。

---

## 8.8 联网补充检索

### 功能说明

当本地知识库证据不足时，系统应允许联网查询用户提供的优先参考渠道、权威教材和学术论文来源。

### 触发条件

1. 本地检索结果数量不足。
2. 本地检索结果相关性低。
3. Answerability Evaluator 判断证据不足。
4. 用户明确要求联网查询。
5. 问题涉及最新资料或本地知识库未覆盖的资料。

### 联网约束

1. 联网工具使用 **Firecrawl + Trusted Source Whitelist**。
2. 优先搜索用户配置的权威网址。
3. 优先使用官方机构、权威教材和学术论文。
4. 不应默认把普通网页作为高可信法律依据。
5. 联网结果应标记来源类型和可信等级。
6. 联网结果进入答案前应经过摘要、证据构建和引用校验。
7. 联网资料不得覆盖本地权威案例 PDF 的优先级。

### 验收标准

1. 系统能够在本地知识不足时触发联网补充。
2. 联网结果应显示 URL、标题、来源类型和摘要。
3. 系统应记录 fallback 是否触发及触发原因。
4. 联网资料不得覆盖本地权威案例 PDF 的优先级。

---

## 9. MCP-style 工具层需求

### 9.1 设计目标

系统应设计 MCP-style 工具层，将外部资料检索、PDF 解析、Citation 验证和评测工具标准化封装，使 Agent 能够通过统一接口调用不同能力。

本项目不要求一开始完整实现 MCP Server，但需求层面应按照 MCP-style 的思想进行工具解耦和接口标准化。所有工具输入输出应使用 Pydantic Schema 或 JSON Schema 约束，保证后续能够平滑迁移为真正的 MCP Server / Client 架构。

### 9.2 工具类型

| 工具 | 职责 | 最终技术实现 |
|---|---|---|
| PDF Parser Tool | 解析 PDF，抽取页码、段落号、标题和正文 | PyMuPDF + pypdf + PaddleOCR fallback |
| Local Knowledge Base Tool | 查询本地案例 PDF 知识库 | PostgreSQL metadata + Milvus + Elasticsearch |
| Hybrid Retrieval Tool | 执行 BM25 + 向量检索 + reranker | Elasticsearch + Milvus + bge-reranker-v2-m3 |
| Official / Trusted Web Search Tool | 查询用户指定权威网址、教材和论文来源 | Firecrawl + sources.yaml whitelist |
| Citation Verification Tool | 验证答案引用是否来自 evidence | Pydantic schema + rule-based check + LLM-assisted check |
| Evaluation Tool | 计算 RAGAS 和自定义指标 | RAGAS + custom metrics scripts |
| Logging Tool | 记录检索、生成、引用和评测日志 | PostgreSQL + Langfuse |

### 9.3 工具输入输出规范示例

#### Citation Verification Tool

输入：

```json
{
  "answer": "string",
  "citations": [],
  "evidence_pack": []
}
```

输出：

```json
{
  "status": "passed | partial | failed",
  "unsupported_claims": [],
  "invalid_citations": [],
  "suggested_action": "accept | revise_answer | retrieve_more"
}
```

#### Evaluation Tool

输入：

```json
{
  "question": "string",
  "answer": "string",
  "contexts": [],
  "citations": [],
  "ground_truth": "string | null"
}
```

输出：

```json
{
  "faithfulness": 0.0,
  "answer_relevance": 0.0,
  "context_precision": 0.0,
  "context_recall": 0.0,
  "citation_accuracy": 0.0,
  "fallback_trigger_accuracy": 0.0
}
```

### 9.4 验收标准

1. 系统核心能力应以工具接口形式封装。
2. Agent 工作流不应直接耦合具体实现细节。
3. 工具输入输出应使用 Pydantic 或 JSON Schema 约束。
4. 后续能够平滑升级为真正的 MCP Server / Client 架构。

---

## 10. Agentic RAG 工作流需求

### 10.1 核心流程

```text
User Query
→ Query Classifier
→ Query Rewrite
→ Legal Intent Router
→ Hybrid Retrieval
→ Evidence Pack Builder
→ Answerability Evaluator
→ Legal Reasoning Generator
→ Citation Verifier
→ Final IRAC Answer
→ Evaluation & Logging
```

若本地知识不足：

```text
Answerability Evaluator
→ Trusted Web Search Tool
→ Web Evidence Builder
→ Legal Reasoning Generator
→ Citation Verifier
→ Final IRAC Answer
```

### 10.2 LangGraph 状态设计

```python
class PublicLawRAGState(TypedDict):
    trace_id: str
    user_query: str
    query_language: str
    query_type: str
    rewritten_queries: dict
    filters: dict
    bm25_results: list
    vector_results: list
    fused_results: list
    reranked_results: list
    evidence_pack: list
    answerability_result: dict
    web_fallback_result: dict | None
    draft_answer: str
    verified_citations: list
    citation_verification_result: dict
    final_answer: str
    evaluation_result: dict
    errors: list
```

### 10.3 Query Classifier

识别问题类型：

1. concept_explanation
2. case_search
3. case_summary
4. rule_analysis
5. treaty_interpretation
6. case_comparison
7. exam_answer
8. citation_lookup
9. unsupported_or_unclear

### 10.4 Answerability Evaluator

输出结构：

```json
{
  "answerability": "answerable | partially_answerable | unanswerable",
  "source_sufficiency": 0.0,
  "citation_confidence": 0.0,
  "needs_web_fallback": true,
  "reason": "string"
}
```

### 10.5 Legal Reasoning Generator

默认生成英文 IRAC：

```text
Issue
Rule
Application
Conclusion
Sources
```

### 10.6 Citation Verifier

校验内容：

1. 引用是否来自本次 evidence pack。
2. 文档标题是否正确。
3. 页码是否存在。
4. 段落号是否存在。
5. 原句是否支持答案中的关键 claim。
6. 是否存在 unsupported claim。

### 10.7 条件边设计

```text
answerability = answerable
→ Legal Reasoning Generator

answerability = partially_answerable / unanswerable
→ Trusted Web Search Tool

citation_verification = passed
→ Final Answer

citation_verification = partial
→ Revise Answer

citation_verification = failed
→ Retrieve More / Regenerate Answer
```

---

## 11. 最终技术栈选型

### 11.1 总表

| 层级 | 最终选型 | 说明 |
|---|---|---|
| 后端服务 | FastAPI | 提供文档、问答、检索、引用、评测 API |
| 前端展示 | Streamlit | 作为简历项目和演示前端，不承载核心业务逻辑 |
| 工作流编排 | LangGraph | 编排 Query Classifier、Hybrid Retrieval、Answerability Evaluator、Citation Verifier 等节点 |
| 数据校验 | Pydantic v2 | 约束 API、工具、工作流状态和评测输出 |
| PDF 主解析 | PyMuPDF | 抽取文本、页码、block、line、span 和页面结构 |
| PDF 辅助处理 | pypdf | 读取元数据、页数、拆分、合并等辅助任务 |
| 复杂文档兜底 | Unstructured | 复杂版式或 PyMuPDF 失败时兜底 |
| OCR | PaddleOCR | 处理扫描页和文本抽取失败页面 |
| Embedding | BAAI/bge-m3 | 支持多语言、长文本和跨语言法律检索 |
| 向量数据库 | Milvus Lite / Milvus Standalone | 开发阶段用 Lite，最终展示用 Standalone |
| 向量类型 | FLOAT_VECTOR | 默认使用 float embedding，不将 binary vector 作为主方案 |
| 向量相似度 | COSINE / Inner Product | 用于 dense retrieval |
| 关键词检索算法 | BM25 | 精确匹配法律术语、案例名、条约条文 |
| 关键词检索系统 | Elasticsearch | 构建可过滤、可高亮、可扩展的全文索引 |
| Reranker | BAAI/bge-reranker-v2-m3 | 对 BM25 + Dense 召回候选段落进行重排 |
| 业务数据库 | PostgreSQL | 保存文档、chunk、引用、问答、日志、评测结果 |
| ORM / Migration | SQLAlchemy 2.0 + Alembic | 管理数据库模型和迁移 |
| 缓存 / 临时状态 | Redis，可选 | 缓存 session、检索结果和临时任务状态 |
| LLM 接入 | OpenAI-compatible API / Qwen API / DeepSeek API | 通过统一 provider 层调用 |
| 联网补充 | Firecrawl + Trusted Source Whitelist | 仅查询配置的权威来源 |
| 评测 | RAGAS + Custom Citation Metrics | 通用 RAG 指标 + 法律 citation 指标 |
| 可观测性 | Langfuse | 记录 prompt、retrieval、generation、verification、evaluation trace |
| 部署 | Docker Compose | 管理 FastAPI、PostgreSQL、Milvus、Elasticsearch、Redis 等服务 |
| 配置管理 | YAML + .env | 管理模型、检索参数、prompt、评测指标和可信来源 |

### 11.2 原型技术与最终选型对照

| 模块 | 原型技术 | 最终版建议 | 是否替换 |
|---|---|---|---|
| 前端 | Streamlit | Streamlit | 保留 |
| 后端 | Streamlit 内部逻辑 | FastAPI | 新增 |
| 工作流 | CrewAI Flow | LangGraph | 建议替换 |
| PDF 解析 | pypdf | PyMuPDF + pypdf | 替换主解析器 |
| OCR | 无 / 不明确 | PaddleOCR | 新增 |
| Embedding | bge-large-en-v1.5 | bge-m3 | 替换 |
| 向量库 | Milvus Lite | Milvus Lite / Milvus Standalone | 保留并升级 |
| 向量类型 | Binary Vector | Float Vector | 替换主方案 |
| 相似度 | Hamming | Cosine / Inner Product | 替换主方案 |
| 关键词检索 | 无 | Elasticsearch BM25 | 新增 |
| Reranker | 无 / 弱 | bge-reranker-v2-m3 | 新增 |
| 联网检索 | Firecrawl | Firecrawl + Trusted Sources | 保留并约束 |
| 数据库 | 无完整业务库 | PostgreSQL | 新增 |
| 日志 | 基础日志 | PostgreSQL + Langfuse | 升级 |
| 评测 | LLM-as-Judge | RAGAS + 自定义 Citation Metrics | 升级 |
| 配置 | settings.py | YAML + .env | 升级 |

### 11.3 关键技术边界

1. **BM25 与 Elasticsearch 的关系**：BM25 是关键词检索算法，Elasticsearch 是承载 BM25 的全文检索系统。MVP 可用 `rank-bm25` 或 `bm25s`，最终版使用 Elasticsearch。
2. **Milvus 与 PostgreSQL 的关系**：Milvus 只负责向量索引，PostgreSQL 负责业务数据、元数据、日志和评测结果。
3. **Elasticsearch 与 PostgreSQL 的关系**：Elasticsearch 只负责全文检索索引，不作为文档主库。
4. **Binary Vector 的定位**：binary quantization 可作为检索压缩实验方案，但不作为最终主检索链路。
5. **Streamlit 的定位**：Streamlit 仅作为演示前端，不直接承载核心业务逻辑。
6. **CrewAI Flow 的定位**：CrewAI Flow 仅作为原型历史方案，最终主工作流使用 LangGraph。
7. **LLM-as-Judge 的定位**：可作为辅助判断方式，但最终评测必须包含可计算的 RAGAS 和 citation 指标。

---

## 12. 数据库与存储架构需求

### 12.1 PostgreSQL 职责

PostgreSQL 作为业务主数据库，负责保存：

1. 文档级元数据
2. 页级文本
3. chunk 元数据
4. citation anchor
5. 问答会话
6. 问答消息
7. 检索结果
8. 答案实际引用
9. 模型调用记录
10. LangGraph 节点状态摘要
11. Langfuse trace id 映射
12. 评测结果
13. 错误日志

### 12.2 Milvus 职责

Milvus 仅负责向量索引和语义召回：

1. 保存 chunk embedding。
2. 支持按 query embedding 语义召回。
3. 支持按 doc_id、legal_domain、document_type 等字段过滤。
4. 返回 chunk_id 和相似度分数。

Milvus 不作为业务数据库，不保存完整问答日志和评测日志。

### 12.3 Elasticsearch 职责

Elasticsearch 负责关键词全文检索：

1. 案例名称精确匹配。
2. 条约条文精确匹配。
3. 法律术语匹配。
4. 段落号或页码查找。
5. 高亮命中片段。
6. 支持 metadata filter。

Elasticsearch 不作为业务数据库，最终结果仍通过 chunk_id 回查 PostgreSQL。

### 12.4 原始文件存储

原始 PDF 文件保存在本地文件系统或对象存储中：

```text
storage/
├── raw_pdfs/
├── parsed_pages/
├── ocr_outputs/
└── exports/
```

数据库仅保存 `file_path`、`source_url`、hash、parse status 和 index status。

### 12.5 核心表设计

| 表名 | 作用 |
|---|---|
| documents | 保存文档级元数据 |
| document_pages | 保存页级文本 |
| document_chunks | 保存检索 chunk |
| citation_anchors | 保存引用锚点 |
| qa_sessions | 保存问答会话 |
| qa_messages | 保存用户问题和系统回答 |
| retrieval_results | 保存每次检索结果 |
| answer_citations | 保存答案实际引用 |
| model_runs | 保存模型调用记录 |
| trace_logs | 保存完整调用链摘要 |
| evaluation_logs | 保存评测结果 |
| error_logs | 保存错误日志 |

---

## 13. API 需求

### 13.1 文档 API

```text
POST /documents/upload
GET /documents
GET /documents/{doc_id}
POST /documents/{doc_id}/parse
POST /documents/{doc_id}/index
DELETE /documents/{doc_id}
```

### 13.2 问答 API

```text
POST /qa/ask
GET /qa/sessions
GET /qa/sessions/{session_id}
GET /qa/messages/{message_id}
```

### 13.3 检索 API

```text
POST /retrieval/search
POST /retrieval/hybrid-search
POST /retrieval/rerank
```

### 13.4 引用 API

```text
GET /citations/{citation_id}
POST /citations/verify
```

### 13.5 评测 API

```text
POST /evaluation/run
GET /evaluation/runs
GET /evaluation/runs/{run_id}
```

### 13.6 系统观测 API

```text
GET /logs/traces/{trace_id}
GET /logs/qa/{message_id}
GET /logs/errors
```

---

## 14. 前端需求

### 14.1 页面结构

Streamlit 前端应包含：

1. 文档上传页
2. 知识库管理页
3. 问答页
4. 案例检索页
5. 案例对比页
6. 引用详情展示区
7. 基础日志 / 评测结果展示区

### 14.2 问答页要求

问答页应支持：

1. 输入问题。
2. 选择是否启用联网补充。
3. 选择法律领域或文档范围。
4. 展示英文 IRAC 答案。
5. 展示 Sources。
6. 展示引用卡片，包括文档标题、页码、段落号、原句。
7. 展示是否触发联网 fallback。
8. 展示 trace ID、基础耗时、token usage。
9. 展示 Citation Verification 结果。
10. 展示 RAGAS / 自定义指标摘要。

### 14.3 前端与后端关系

Streamlit 不直接执行 PDF 解析、模型调用、检索和数据库写入。Streamlit 只通过 HTTP / JSON 调用 FastAPI。

---

## 15. 评测与日志需求

### 15.1 基础日志

每次问答应记录：

1. 用户问题
2. 问题类型
3. query rewrite 结果
4. BM25 检索结果
5. 向量检索结果
6. fusion 结果
7. reranker 排序结果
8. 最终使用的 evidence pack
9. Answerability Evaluator 输出
10. 是否触发联网 fallback
11. fallback 触发原因
12. 模型输入 prompt
13. 模型输出答案
14. 引用来源
15. citation verification 结果
16. RAGAS 评测结果
17. 自定义指标结果
18. 响应时间
19. token 消耗
20. 错误信息

### 15.2 Langfuse Trace

Langfuse 应记录以下节点：

1. Query Classifier
2. Query Rewrite
3. BM25 Retrieval
4. Vector Retrieval
5. Reranker
6. Evidence Pack Builder
7. Answerability Evaluator
8. Trusted Web Search Tool
9. Legal Reasoning Generator
10. Citation Verifier
11. Evaluation Tool
12. Final Answer

### 15.3 RAGAS 评测指标

系统应支持以下 RAGAS 指标：

1. Faithfulness
2. Answer Relevance
3. Context Precision
4. Context Recall

### 15.4 自定义评测指标

系统应支持以下自定义指标：

1. Citation Accuracy
2. Paragraph Match Rate
3. Source Grounding Rate
4. Unsupported Claim Rate
5. Fallback Trigger Accuracy
6. Retrieval Hit Rate
7. Latency
8. Token Usage

### 15.5 指标解释

| 指标 | 说明 |
|---|---|
| Citation Accuracy | 答案中的引用是否真实存在并支持对应结论 |
| Paragraph Match Rate | 引用段落号是否与原文匹配 |
| Source Grounding Rate | 答案关键 claim 是否有来源支持 |
| Unsupported Claim Rate | 没有证据支持的结论比例 |
| Fallback Trigger Accuracy | 系统是否在本地证据不足时正确触发联网补充 |
| Retrieval Hit Rate | 检索结果是否命中预期来源 |
| Latency | 系统响应时间 |
| Token Usage | 单次问答 token 消耗 |

### 15.6 验收标准

1. 系统能够为每次问答生成 trace ID。
2. 系统能够保存检索、生成、引用和评测日志。
3. 系统能够计算基础 RAGAS 指标。
4. 系统能够计算 Citation Accuracy。
5. 系统能够记录 Fallback Trigger Accuracy 所需数据。
6. 系统能够在 Streamlit 中展示 trace ID、引用校验结果和评测摘要。

---

## 16. 非功能需求

### 16.1 可追溯性

每个关键法律结论应尽量绑定来源。引用至少包含文档标题、页码和原句；若可识别段落号，应包含段落号。

### 16.2 可靠性

当本地知识库和联网补充均无法提供充分证据时，系统应明确说明资料不足，不得编造结论。

### 16.3 可维护性

系统应支持新增 PDF、重新解析、重新索引、修改元数据和查看日志。

### 16.4 可扩展性

系统应预留扩展能力，包括新增数据来源、新增检索器、新增 reranker、新增评测指标和升级为真正 MCP Server / Client 架构。

### 16.5 可评估性

系统应记录每次问答的检索、生成、引用校验和评测数据，为后续实验与简历展示提供支撑。

### 16.6 可配置性

模型、检索参数、权威来源、prompt 模板、评测指标应尽量通过配置文件管理。

### 16.7 可观测性

系统应通过 Langfuse 和 PostgreSQL 日志记录工作流运行状态，支持定位检索失败、引用错误、fallback 误触发和回答生成异常。

---

## 17. 配置管理需求

建议使用 YAML 管理配置：

```text
config/
├── sources.yaml       # 可信联网来源白名单与可信等级
├── models.yaml        # LLM、Embedding、Reranker 配置
├── retrieval.yaml     # BM25、向量检索、fusion、rerank 参数
├── prompts.yaml       # IRAC、case brief、concept explanation 等 prompt
├── evaluation.yaml    # RAGAS 与自定义指标配置
├── database.yaml      # PostgreSQL / Milvus / Elasticsearch 配置
└── app.yaml           # 应用级配置
```

敏感信息使用 `.env` 管理：

```text
OPENAI_API_KEY=
QWEN_API_KEY=
DEEPSEEK_API_KEY=
FIRECRAWL_API_KEY=
DATABASE_URL=
MILVUS_URI=
ELASTICSEARCH_URL=
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
```

---

## 18. 核心项目亮点

### 18.1 法律结构感知 PDF 解析

系统不是简单抽取 PDF 文本，而是尽量保留页码、段落号、章节标题和原文片段，为后续 citation 提供基础。

### 18.2 Agentic RAG 工作流

系统通过 Query Classifier、Legal Intent Router、Answerability Evaluator、Citation Verifier 等模块，将普通 RAG 升级为可路由、可判断、可校验的 Agentic RAG。

### 18.3 MCP-style 工具层

系统将 PDF 解析、本地检索、联网补充、引用校验和评测能力标准化封装，为后续升级到 MCP Server / Client 架构预留空间。

### 18.4 段落级可追溯引用

系统要求答案引用精确到文档标题、页码、段落号或原句，降低大模型在法律问答中的虚构引用风险。

### 18.5 Hybrid Retrieval

系统采用 Elasticsearch BM25 + BGE-M3 dense retrieval + bge-reranker-v2-m3 的混合检索链路，同时兼顾法律术语精确匹配和跨语言语义召回。

### 18.6 评测闭环

系统不仅生成答案，还记录检索、生成、引用校验和 fallback 行为，并通过 RAGAS 与自定义指标评估系统可靠性。

### 18.7 全流程可观测

系统接入 Langfuse，记录 query rewrite、retrieval、rerank、generation、citation verification 和 evaluation 的关键 trace。

---

## 19. 最终系统核心流程

```text
提前爬取案例 PDF
→ PDF 上传 / 入库
→ PyMuPDF 结构化解析
→ PaddleOCR 扫描页兜底
→ 页码 / 段落号 / 原句提取
→ Chunk 生成
→ Citation Anchor 生成
→ PostgreSQL 保存文档、页、chunk、引用锚点
→ Elasticsearch BM25 索引构建
→ BGE-M3 Embedding 生成
→ Milvus 向量索引构建
→ 用户输入问题
→ FastAPI 接收请求
→ LangGraph 启动 Agentic RAG 工作流
→ Query Classifier
→ Query Rewrite
→ Hybrid Retrieval
→ Reranker
→ Evidence Pack Builder
→ Answerability Evaluator
→ 必要时 Trusted Web Search
→ Legal Reasoning Generator
→ Citation Verifier
→ Final English IRAC Answer
→ Sources 展示
→ RAGAS / Custom Metrics Evaluation
→ PostgreSQL Logging
→ Langfuse Trace
```

---

## 20. 开发优先级建议：从原型升级到最终版

### Phase 1：原型工程化改造

目标：将当前 Streamlit demo 改造为前后端分离的工程结构。

1. 保留 Streamlit 作为演示前端。
2. 新增 FastAPI 后端。
3. 将原 Streamlit 内部逻辑迁移为 API 服务。
4. 新增 PostgreSQL 保存 documents、document_chunks、qa_sessions、qa_messages、retrieval_results。
5. 保留 Milvus Lite 完成基础向量检索闭环。
6. 建立统一 Pydantic Schema。
7. 建立 `config/` 与 `.env` 配置体系。

### Phase 2：PDF 解析与引用增强

目标：支撑段落级 citation。

1. 将主解析器从 pypdf 升级为 PyMuPDF。
2. 保留页码、段落号、章节标题和原句。
3. 增加 PaddleOCR 扫描页兜底。
4. 生成 Citation Anchor。
5. 实现 Citation Formatter。
6. 实现 Citation Verifier 的初版规则校验。

### Phase 3：Hybrid Retrieval 升级

目标：从单向量检索升级为法律场景更稳定的混合检索。

1. Embedding 从 bge-large-en-v1.5 升级为 BAAI/bge-m3。
2. 向量检索从 binary vector 升级为 float vector。
3. 新增 Elasticsearch BM25。
4. 实现 BM25 + Dense Retrieval。
5. 实现 RRF 或 weighted fusion。
6. 新增 BAAI/bge-reranker-v2-m3。
7. 形成 BM25 + Dense + Reranker 的 Evidence Pack 构建链路。

### Phase 4：LangGraph Agentic RAG

目标：从普通 RAG 升级为可路由、可判断、可校验的 Agentic RAG。

1. 用 LangGraph 编排 Query Classifier、Query Rewrite、Legal Intent Router。
2. 实现 Evidence Pack Builder。
3. 实现 Answerability Evaluator。
4. 将 Firecrawl 改造成 Trusted Web Search Tool。
5. 实现本地证据不足时的条件路由。
6. 将 Citation Verifier 接入生成后校验节点。
7. 支持 citation failed 时重新生成或重新检索。

### Phase 5：评测与展示

目标：让项目适合简历、答辩和面试展示。

1. 接入 Langfuse。
2. 接入 RAGAS。
3. 实现 Citation Accuracy。
4. 实现 Paragraph Match Rate。
5. 实现 Fallback Trigger Accuracy。
6. 实现 Streamlit evaluation dashboard。
7. 完善 README、架构图、demo 截图和测试样例。

---

## 21. 验收标准总览

最终版本应满足以下验收标准：

1. 能够上传并解析国际公法案例 PDF。
2. 能够将 PDF 文本切分为带页码、段落号或原句的 chunk。
3. 能够构建本地知识库和检索索引。
4. 能够基于本地案例 PDF 进行英文 IRAC 问答。
5. 能够返回文档标题、页码、段落号 / 原句级引用。
6. 能够进行案例检索与结构化 case brief 生成。
7. 能够进行国际公法概念解释。
8. 能够进行案例对比。
9. 能够在本地知识不足时联网补充查询指定权威渠道。
10. 能够通过 MCP-style 工具层标准化封装核心能力。
11. 能够通过 LangGraph 编排 Agentic RAG 工作流。
12. 能够记录问答、检索、生成、引用和 fallback 日志。
13. 能够计算 RAGAS、Citation Accuracy 和 Fallback Trigger Accuracy。
14. 能够通过 FastAPI 提供后端接口。
15. 能够通过 Streamlit 提供演示前端。
16. 能够通过 Langfuse 查看关键 trace。
17. 项目能够作为“大模型 Agent 应用”岗位的简历展示项目，体现 RAG、Agent Workflow、Citation Verification、MCP-style Tool Layer、Hybrid Retrieval、Evaluation 和 Observability 的综合能力。

---

## 22. 简历表达方向

### 22.1 项目一句话

基于 FastAPI、Streamlit、LangGraph、Embedding、Hybrid RAG、MCP-style 工具层和大模型 API，构建面向国际公法案例 PDF 的 Agentic RAG 英文研究助手，支持 IRAC 法律问答、段落级引用、案例摘要、案例对比、联网补充和评测日志。

### 22.2 简历技术亮点

1. 设计法律结构感知 PDF 解析与 chunk 策略，基于 PyMuPDF 保留文档标题、页码、段落号和原句，支撑国际公法问答中的可追溯 citation。
2. 实现 Elasticsearch BM25 + BGE-M3 Dense Retrieval + bge-reranker-v2-m3 的混合检索链路，提高案例名称、法律术语和跨语言语义问题的证据召回质量。
3. 构建 LangGraph Agentic RAG 工作流，引入 Query Classifier、Answerability Evaluator、Trusted Web Search 和 Citation Verifier，根据证据充分性动态路由。
4. 设计 MCP-style 工具层，将 PDF 解析、本地检索、联网补充、引用验证和评测工具标准化封装，提高系统扩展性。
5. 接入 RAGAS 与自定义 Citation Accuracy / Fallback Trigger Accuracy 指标，记录检索、生成、引用和 fallback 过程，形成基础评测闭环。
6. 使用 PostgreSQL 管理文档元数据、chunk、citation anchor、问答日志和评测结果，并接入 Langfuse 实现全流程可观测。

---

## 23. 总结

Agentic RAG 国际公法研究助手的核心价值在于：

```text
让大模型不再凭内部知识自由回答法律问题，
而是在国际公法案例 PDF、权威资料、结构化检索、引用校验和评测日志的约束下，
生成可追溯、可验证、可评估的英文法律分析答案。
```

本系统适合作为大模型 Agent 应用方向的简历项目，能够体现法律场景建模、RAG 工程、Agent 工作流、MCP-style 工具封装、Citation Verification、Hybrid Retrieval、Evaluation 和 Observability 等综合能力。
