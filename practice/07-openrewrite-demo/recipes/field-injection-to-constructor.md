# Recipe: Field Injection to Constructor Injection

## Intent

Convert a Spring service that uses `@Autowired` field injection into constructor injection.

## Why teams do this

- constructor injection is easier to test
- dependencies become explicit
- immutability is easier to enforce
- modernization can be applied consistently across many services

## What this demo rewrites

Input shape:

```java
@Autowired
private OrderRepository orderRepository;
```

Output shape:

```java
private final OrderRepository orderRepository;

public LegacyOrderService(OrderRepository orderRepository) {
    this.orderRepository = orderRepository;
}
```

## Mapping to real OpenRewrite usage

In a real repository, this kind of change would usually be expressed as:

- a `rewrite.yml` recipe
- a Maven or Gradle plugin configuration
- a dry run reviewed in pull requests
- a staged rollout across many modules or services

This demo keeps only the core idea:

> express a repeatable refactoring rule, then verify the result mechanically

