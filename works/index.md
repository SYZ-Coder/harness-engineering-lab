# Harness Engineering 原创专题导航

> 这是 `works/` 目录中原创整理内容的统一入口。  
> 现在内容被分成两条主线：`general-agent-engineering/`（通用智能体工程化）和 `microservice-agent-engineering/`（微服务智能体工程化）。

---

## 一、这组内容适合谁

- 想搞清楚 Harness Engineering 到底是什么、又不是什么
- 想在团队或个人项目里真正落地编码智能体的人
- 已经开始用 AI 写代码，但感觉“会用工具，不会建系统”的人
- 正在做 Spring / Java 微服务治理和落地的人

---

## 二、推荐阅读顺序

### 第一部分：`general-agent-engineering/` 通用智能体工程化

1. [Harness Engineering 到底怎么用：从概念到落地实施指南](general-agent-engineering/adoption-guides-and-roadmaps/harness-engineering-how-to-use-and-land.md)
2. [中小团队 AGENTS.md 最小模板](general-agent-engineering/agents-md-templates/mvp-agents-template-for-small-teams.md)
3. [Harness Engineering 的验证闭环](general-agent-engineering/validation-loop-design/harness-validation-loop.md)
4. [4 种 Harness 架构的优缺点与适用场景](general-agent-engineering/adoption-guides-and-roadmaps/harness-architecture-patterns-comparison.md)
5. [团队实施路线图：从试点到平台化](general-agent-engineering/adoption-guides-and-roadmaps/harness-implementation-roadmap-for-teams.md)
6. [Harness Engineering 落地清单](general-agent-engineering/adoption-guides-and-roadmaps/harness-checklist.md)
7. [从零到发布：一个中小团队如何落地 Harness Engineering](general-agent-engineering/adoption-guides-and-roadmaps/from-zero-to-release-tutorial.md)

### 第二部分：`microservice-agent-engineering/` 微服务智能体工程化

8. [Spring Cloud / Java 微服务 Harness 落地蓝图](microservice-agent-engineering/spring-blueprints/spring-microservices-harness-blueprint.md)
9. [Spring 微服务 AGENTS.md 模板](microservice-agent-engineering/spring-blueprints/spring-microservices-agents-template.md)
10. [Spring 微服务契约测试与可观测性 Playbook](microservice-agent-engineering/contract-testing-playbooks/spring-microservices-contract-observability-playbook.md)
11. [Spring 微服务 ArchUnit + 契约检查清单](microservice-agent-engineering/contract-testing-playbooks/spring-microservices-archunit-contract-checklist.md)
12. [微服务团队落地 Harness Engineering 全景指南](microservice-agent-engineering/spring-blueprints/microservices-harness-guide.md)

### 第三部分：可运行示例

13. [最小 Python Harness Demo](../practice/02-minimal-harness-demo/README.md)
14. [Spring 微服务模板 Demo](../practice/03-spring-service-template-demo/README.md)
15. [最小契约测试 Demo](../practice/05-contract-testing-demo/README.md)
16. [最小可观测性 Demo](../practice/06-observability-demo/README.md)
17. [最小 OpenRewrite Demo](../practice/07-openrewrite-demo/README.md)
18. [最小服务目录 Demo](../practice/08-service-catalog-demo/README.md)
19. [最小验证闭环 Demo](../practice/09-validation-review-demo/README.md)

---

## 三、按角色推荐

### 如果你是个人开发者

先读：

1. 总览
2. AGENTS 模板
3. 验证闭环
4. 最小 Python Demo

### 如果你是团队负责人或 TL

先读：

1. 总览
2. 路线图
3. 验证闭环
4. 落地清单

### 如果你是架构师或平台工程师

先读：

1. 总览
2. 微服务蓝图
3. 契约与可观测性 Playbook
4. 微服务全景指南

---

## 四、如果你只想快速上手

可以直接按这个顺序：

1. 总览
2. AGENTS 模板
3. 验证闭环
4. 一个 Demo

核心原则是：

> **先跑通最小闭环，再考虑更复杂的系统。**

