# practice/ — 动手实践

选一个小项目，用 Harness Engineering 的方法论从零构建，验证原文中的经验。

## 文件约定

- 每个实验一个子目录，如 `practice/01-cli-tool/`
- 每个实验包含：README.md（目标与方法）、AGENTS.md（给智能体的指导）、代码
- 关键：人类只写提示词和约束，代码全部由智能体生成

## 实验建议

| 实验 | 验证的概念 | 复杂度 |
|------|-----------|--------|
| 用 Claude Code 生成一个 CLI 工具 | 仓库即记录系统 + AGENTS.md 设计 | ⭐ |
| 为生成的代码写自定义 linter | 机械化执行 | ⭐⭐ |
| 让智能体自己重构自己写的代码 | 熵管理与垃圾回收 | ⭐⭐⭐ |

## 已有实验

| 目录 | 说明 |
|------|------|
| [01-ralph-demo/](01-ralph-demo/) | 用 Ralph Orchestrator 跑完整编排循环，验证角色分工、背压门控与持久记忆 |
| [02-minimal-harness-demo/](02-minimal-harness-demo/) | 最小可运行 Harness Demo，验证 AGENTS、PROMPT、测试门控与可复用样板 |
| [03-spring-service-template-demo/](03-spring-service-template-demo/) | Spring 微服务模板 Demo，验证分层约束、契约文件与 ArchUnit 规则 |
| [05-contract-testing-demo/](05-contract-testing-demo/) | 最小契约测试 Demo，验证 provider verification 与 consumer 兼容性检查 |
| [06-observability-demo/](06-observability-demo/) | 最小可观测性 Demo，验证 trace id 贯通、日志关联与跨服务链路可见性 |
| [07-openrewrite-demo/](07-openrewrite-demo/) | 最小 OpenRewrite Demo，验证批量治理、确定性重写与历史写法演进 |
| [08-service-catalog-demo/](08-service-catalog-demo/) | 最小服务目录 Demo，验证平台元数据、仓库自描述与 owner/API/依赖入口 |
| [09-validation-review-demo/](09-validation-review-demo/) | 最小验证闭环 Demo，验证 lint、测试、AI review 与人工 review 的组合 |

## 下一步

实践中踩坑了？建议直接在仓库中补充新的实践 README、清单，或通过 Issue / PR 记录反馈。

