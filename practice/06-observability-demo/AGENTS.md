# AGENTS.md

## Project Role

- This demo shows the minimum observability pattern for service-to-service workflows.
- It focuses on trace id propagation, log correlation, and request path visibility.
- It does not attempt to run a full telemetry backend.

## Project Map

- `README.md`：demo overview and usage
- `services/gateway_service.py`：entry-point service
- `services/order_service.py`：downstream service
- `shared/tracing.py`：trace context and logging helpers
- `tests/test_observability_demo.py`：verification tests

Start here:

- Read `README.md`
- Read `shared/tracing.py`
- Run tests before modifying behavior

## Working Rules

- Keep the demo standard-library only
- Preserve trace id propagation across service boundaries
- Keep logs readable and structured

## Hard Constraints

- Do not remove trace id from responses or logs
- Do not bypass the tracing helper functions
- Do not add unnecessary framework complexity

## Verification

- `python -m unittest discover -s tests -p "test_*.py"`

