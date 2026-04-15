# AGENTS.md

## Repository Role

- This repository is a standalone, open-source practice repository for Harness Engineering.
- It focuses on practical adoption materials: guides, templates, playbooks, checklists, and runnable demos.
- The structure is intentionally split into general agent engineering and microservice agent engineering.

## Project Map

- `README.md`：project homepage for GitHub readers
- `INDEX.md`：quick reading map
- `works/general-agent-engineering/`：通用智能体工程化内容，包含总览、模板、路线图和验证闭环
- `works/microservice-agent-engineering/`：微服务智能体工程化内容，包含 Spring 蓝图、契约测试和可观测性主题
- `practice/`：runnable demos and templates
- `LICENSE`：open-source license

Start here:

- New readers: `README.md`
- Want the reading order: `INDEX.md`
- Want templates and guides: `works/`
- Want runnable examples: `practice/`

## Working Rules

- Keep documents standalone and publishable.
- Prefer practical guidance over abstract commentary.
- When adding demos, include a README and verification instructions.
- Keep templates concise and reusable.

## Hard Constraints

- Do not assume readers have access to the original source repository.
- Do not introduce repo-specific references without explanation.
- Do not add placeholder files without clear value.

## Verification

- Python demos:
  - `python -m unittest discover -s practice\02-minimal-harness-demo\tests -p "test_*.py"`
  - `python -m unittest discover -s practice\05-contract-testing-demo\tests -p "test_*.py"`
  - `python -m unittest discover -s practice\06-observability-demo\tests -p "test_*.py"`
  - `python -m unittest discover -s practice\07-openrewrite-demo\tests -p "test_*.py"`
  - `python -m unittest discover -s practice\08-service-catalog-demo\tests -p "test_*.py"`
  - `python practice\09-validation-review-demo\tools\validate_demo.py`
  - `python -m unittest discover -s practice\09-validation-review-demo\tests -p "test_*.py"`
- Java demo:
  - `mvn test` in `practice\03-spring-service-template-demo`

