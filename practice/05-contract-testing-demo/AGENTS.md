# AGENTS.md

## Project Role

- This demo shows a minimal contract-testing workflow for service-to-service integration.
- It is intentionally lightweight and uses Python standard library only.
- The goal is to demonstrate the idea of provider verification, not to recreate a full Pact platform.

## Project Map

- `contracts/order-response-contract.json`：the contract source of truth
- `provider/order_provider.py`：provider-side response implementation
- `consumer/order_client.py`：consumer-side parsing logic
- `tests/test_contract_demo.py`：contract verification and compatibility tests
- `README.md`：usage and explanation

Start here:

- Read `README.md`
- Read the contract file before reading code
- Run tests before making changes

## Working Rules

- Keep the contract file readable and explicit
- Do not change provider shape without updating contract and tests
- Prefer standard library only

## Hard Constraints

- Do not bypass the contract file
- Do not remove compatibility checks from tests
- Do not change response structure silently

## Verification

- `python -m unittest discover -s tests -p "test_*.py"`

