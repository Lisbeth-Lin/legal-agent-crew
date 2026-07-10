# 22. Business Functions Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

在通用 RAG 工作流之上实现案例摘要、概念解释、案例对比等国际公法业务功能。

## 2. 前置依赖

LangGraph Workflow, Retrieval, Generator。

## 3. 交付物

- case brief
- concept explanation
- case comparison

## 4. 最小任务 Checklist

- [ ] BF-01 实现 Case Search：按案件名称、机构、年份、法律领域查询相关文档和 chunks。
- [ ] BF-02 实现 Case Summary / Case Brief 输出模板：Case Name、Institution、Year、Facts、Issues、Applicable Law、Reasoning、Holding、Key Paragraphs、Teaching Value、Sources。
- [ ] BF-03 实现 Concept Explanation 输出模板：Concept、One-sentence Explanation、Legal Sources、Leading Cases、Distinction、Misunderstandings、Exam/Research Usage、Sources。
- [ ] BF-04 实现 Case Comparison 检索策略：对每个案例分别检索，再按对比维度组织 Evidence Pack。
- [ ] BF-05 实现 Case Comparison 表格输出：Facts、Legal Issues、Applicable Rules、Reasoning、Conclusion、Subsequent Influence。
- [ ] BF-06 为每种业务功能配置专用 prompt，但仍复用 Citation Verifier。
- [ ] BF-07 将业务功能接入 /qa/ask 的 query_type 路由。

## 5. 独立测试 Checklist

- [ ] TEST-01 输入 case_summary 问题返回 case brief 模板。
- [ ] TEST-02 输入 concept_explanation 问题返回概念解释模板。
- [ ] TEST-03 输入两个案例对比问题返回表格。
- [ ] TEST-04 所有业务输出都包含 Sources。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
