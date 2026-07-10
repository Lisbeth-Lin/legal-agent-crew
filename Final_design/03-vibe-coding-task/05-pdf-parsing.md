# 05. PDF Parsing Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

使用 PyMuPDF 为主解析 PDF，保留页码、段落号、章节标题、原句和 citation anchor。

## 2. 前置依赖

Document Upload, Database Models。

## 3. 交付物

- 页级文本
- chunk 文本
- citation anchors
- 解析日志

## 4. 最小任务 Checklist

- [ ] PP-01 实现 PDFParserService.parse_document(doc_id)。
- [ ] PP-02 用 PyMuPDF 逐页提取文本 block、line、span，并保留 page_number。
- [ ] PP-03 实现空页、乱码页、字符过少页检测。
- [ ] PP-04 接入 PaddleOCR fallback，对扫描页生成 OCR 文本，并标记 parse_method=ocr。
- [ ] PP-05 保留 pypdf 用于 PDF 元数据、页数校验和辅助读取。
- [ ] PP-06 实现段落号识别规则：para. 12、[12]、12.、Article 31、Section I 等。
- [ ] PP-07 实现章节标题识别：基于大写标题、编号标题、字体/位置特征或规则。
- [ ] PP-08 实现法律语义 chunk 切分：优先按段落号切分，过长段落再按 token window 切分，保留 overlap。
- [ ] PP-09 为每个 chunk 生成 citation_anchor，格式包含 doc_id、page_number、paragraph_number。
- [ ] PP-10 写入 document_pages、document_chunks、citation_anchors 表。
- [ ] PP-11 更新 documents.parse_status 为 success / partial_success / failed。

## 5. 独立测试 Checklist

- [ ] TEST-01 文本型 PDF 能解析出 page_number 和 chunk。
- [ ] TEST-02 带段落号文本能识别 paragraph_number。
- [ ] TEST-03 无段落号 PDF 仍能生成 page-level citation。
- [ ] TEST-04 模拟空页时触发 OCR fallback。
- [ ] TEST-05 解析失败时 parse_status=failed 且 error_logs 有记录。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
