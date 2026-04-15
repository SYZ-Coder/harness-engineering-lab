# harness-engineering-practice

Practical Harness Engineering guides, templates, playbooks, and runnable demos.

This repository is organized around two main tracks:

- General Agent Engineering
- Microservice Agent Engineering

It is designed as a standalone open-source project for people who want to move from:

- "I know the concept"

to:

- "I can actually apply it in a real codebase"

## What is inside

- `works/`
  Guides, templates, playbooks, and checklists
- `practice/`
  Runnable demos
- `INDEX.md`
  Recommended reading path

## Repository structure

```text
harness-engineering-practice/
├── README.md
├── README.en.md
├── LICENSE
├── CONTRIBUTING.md
├── AGENTS.md
├── INDEX.md
├── works/
│   ├── general-agent-engineering/
│   │   ├── adoption-guides-and-roadmaps/
│   │   ├── agents-md-templates/
│   │   └── validation-loop-design/
│   └── microservice-agent-engineering/
│       ├── spring-blueprints/
│       ├── contract-testing-playbooks/
│       └── observability-integration/
└── practice/
    ├── 02-minimal-harness-demo/
    ├── 03-spring-service-template-demo/
    ├── 05-contract-testing-demo/
    ├── 06-observability-demo/
    ├── 07-openrewrite-demo/
    ├── 08-service-catalog-demo/
    └── 09-validation-review-demo/
```

中文说明：

- `README.md` / `README.en.md`：中英文首页
- `INDEX.md`：总阅读索引，适合第一次进入仓库时快速找阅读顺序
- `AGENTS.md`：仓库级入口说明，帮助智能体或维护者理解结构和验证方式
- `CONTRIBUTING.md` / `RELEASE-CHECKLIST.md`：贡献与发布前检查入口
- `works/`：文章、模板、手册、清单、教程
- `works/general-agent-engineering/`：通用智能体工程化内容
- `works/general-agent-engineering/adoption-guides-and-roadmaps/`：总览、路线图、清单、教程与架构对照
- `works/general-agent-engineering/agents-md-templates/`：中小团队仓库入口模板
- `works/general-agent-engineering/validation-loop-design/`：验证闭环与反馈回路设计
- `works/microservice-agent-engineering/`：微服务智能体工程化内容
- `works/microservice-agent-engineering/spring-blueprints/`：Spring / Java 微服务蓝图、模板与总览
- `works/microservice-agent-engineering/contract-testing-playbooks/`：契约测试、结构约束与相关清单
- `works/microservice-agent-engineering/observability-integration/`：可观测性方向的扩展入口
- `practice/`：可运行示例区
- `practice/01-ralph-demo/`：Ralph 编排与多角色循环样板
- `practice/02-minimal-harness-demo/`：最小 Python Harness Demo
- `practice/03-spring-service-template-demo/`：最小 Java / Spring 服务模板 Demo
- `practice/05-contract-testing-demo/`：最小契约测试 Demo
- `practice/06-observability-demo/`：最小可观测性 Demo
- `practice/07-openrewrite-demo/`：最小批量治理 / OpenRewrite 风格 Demo
- `practice/08-service-catalog-demo/`：最小服务目录 Demo
- `practice/09-validation-review-demo/`：最小验证闭环 Demo

## What you will find

### General Agent Engineering

- concept-to-practice guide
- `AGENTS.md` template for small teams
- validation loop design
- architecture comparison
- implementation roadmap
- adoption checklist
- from-zero-to-release tutorial

### Microservice Agent Engineering

- Spring Cloud / Java microservices blueprint
- Spring microservices `AGENTS.md` template
- contract testing and observability playbook
- ArchUnit + contract checklist
- microservices adoption guide

### Runnable demos

- `practice/02-minimal-harness-demo`
  A tiny Python demo showing task file + `AGENTS.md` + tests as a minimal Harness loop
- `practice/03-spring-service-template-demo`
  A minimal Java microservice-style template showing layering, ArchUnit checks, contract file placement, and OTel notes
- `practice/05-contract-testing-demo`
  A minimal contract-testing demo showing provider verification and consumer compatibility checks
- `practice/06-observability-demo`
  A minimal observability demo showing trace-id propagation, log correlation, and cross-service flow visibility
- `practice/07-openrewrite-demo`
  A minimal OpenRewrite-style demo showing batch modernization, deterministic rewrites, and legacy-code evolution
- `practice/08-service-catalog-demo`
  A minimal service-catalog demo showing platform metadata, repository self-description, and owner/API/dependency entry points
- `practice/09-validation-review-demo`
  A minimal validation-loop demo showing lint, tests, AI review, and human review as separate feedback layers

## Recommended reading path

1. `works/index.md`
2. `works/general-agent-engineering/adoption-guides-and-roadmaps/harness-engineering-how-to-use-and-land.md`
3. `works/general-agent-engineering/agents-md-templates/mvp-agents-template-for-small-teams.md`
4. `works/general-agent-engineering/validation-loop-design/harness-validation-loop.md`
5. `works/general-agent-engineering/adoption-guides-and-roadmaps/harness-implementation-roadmap-for-teams.md`
6. `works/general-agent-engineering/adoption-guides-and-roadmaps/harness-checklist.md`
7. `works/microservice-agent-engineering/spring-blueprints/spring-microservices-harness-blueprint.md`
8. `works/microservice-agent-engineering/spring-blueprints/microservices-harness-guide.md`
9. `practice/02-minimal-harness-demo/README.md`
10. `practice/03-spring-service-template-demo/README.md`
11. `practice/05-contract-testing-demo/README.md`
12. `practice/06-observability-demo/README.md`
13. `practice/07-openrewrite-demo/README.md`
14. `practice/08-service-catalog-demo/README.md`
15. `practice/09-validation-review-demo/README.md`

## Quick verification

### Python demos

```bash
python -m unittest discover -s practice\02-minimal-harness-demo\tests -p "test_*.py"
python -m unittest discover -s practice\05-contract-testing-demo\tests -p "test_*.py"
python -m unittest discover -s practice\06-observability-demo\tests -p "test_*.py"
python -m unittest discover -s practice\07-openrewrite-demo\tests -p "test_*.py"
python -m unittest discover -s practice\08-service-catalog-demo\tests -p "test_*.py"
python practice\\09-validation-review-demo\\tools\\validate_demo.py
python -m unittest discover -s practice\09-validation-review-demo\tests -p "test_*.py"
```

### Java demo

```bash
cd practice\03-spring-service-template-demo
mvn test
```

## Project goal

This repository is not meant to present Harness Engineering as abstract theory.

It is meant to help teams:

- write better repository entry files
- add structure and validation around coding agents
- introduce contracts and observability into microservice adoption
- build reusable Harness patterns that teams can actually copy

## License

MIT


