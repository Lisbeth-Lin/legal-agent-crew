# 18. LangGraph Workflow Module Tasks

> 类型：Vibe Coding 最小可执行任务清单

## 1. 模块目标

用 LangGraph 编排完整 Agentic RAG 状态机和条件路由。

## 2. 前置依赖

Query Classifier, Retrieval, Answerability, Generator, Citation Verifier, Evaluation。

## 3. 交付物

- Compiled LangGraph workflow
- RAGWorkflowState

## 4. 最小任务 Checklist

- [ ] LW-01 定义 RAGWorkflowState：question、query_type、rewritten_queries、retrieval_results、evidence_pack、answerability_result、web_evidence、draft_answer、citation_result、final_answer、evaluation_result、trace_id。
- [ ] LW-02 实现 classify_query 节点。
- [ ] LW-03 实现 rewrite_query 节点。
- [ ] LW-04 实现 hybrid_retrieve 节点。
- [ ] LW-05 实现 build_evidence_pack 节点。
- [ ] LW-06 实现 evaluate_answerability 节点。
- [ ] LW-07 实现 trusted_web_search 条件节点。
- [ ] LW-08 实现 generate_irac_answer 节点。
- [ ] LW-09 实现 verify_citations 节点。
- [ ] LW-10 实现 revise_or_retrieve_more 条件处理，限制最大修订次数。
- [ ] LW-11 实现 evaluation_and_logging 终态节点。
- [ ] LW-12 编译 workflow 并提供 run_qa_workflow(question, options)。

## 5. 独立测试 Checklist

- [ ] TEST-01 answerable 分支不触发 web search。
- [ ] TEST-02 unanswerable 分支触发 web search。
- [ ] TEST-03 citation failed 分支触发 revise 或 retrieve_more。
- [ ] TEST-04 最大循环次数限制有效。

## 6. 完成标准

- [ ] 本模块所有最小任务完成。
- [ ] 本模块独立测试全部通过。
- [ ] 本模块没有把其他模块的实现细节硬编码进来。
- [ ] 本模块输入输出使用 Pydantic Schema 或清晰的数据结构约束。
