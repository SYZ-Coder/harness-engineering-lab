# AGENTS.md

## Project Role

- This demo shows a minimal service-catalog pattern for microservice repositories.
- It combines platform-facing metadata and repository-facing self-description.
- It is designed to be readable by humans, coding agents, and internal platforms.

## Project Map

- `README.md`: demo overview and usage
- `catalog-info.yaml`: Backstage-style catalog registration
- `service.yaml`: repository-native service descriptor
- `ownership/owner.md`: owner and contact guidance
- `apis/openapi-order-query.yaml`: API contract sample
- `dependencies/services.yaml`: upstream and downstream dependencies
- `docs/service-overview.md`: service overview for readers
- `tests/test_catalog_demo.py`: metadata verification tests

Start here:

- Read `README.md`
- Compare `catalog-info.yaml` and `service.yaml`
- Read `docs/service-overview.md`
- Run tests before changing metadata structure

## Working Rules

- Keep the demo platform-light and documentation-friendly
- Preserve alignment between `catalog-info.yaml` and `service.yaml`
- Keep the metadata easy for humans and agents to scan quickly

## Hard Constraints

- Do not require a running Backstage instance
- Do not add third-party Python dependencies
- Do not introduce fields that are not explained by the demo

## Verification

- `python -m unittest discover -s tests -p "test_*.py"`

