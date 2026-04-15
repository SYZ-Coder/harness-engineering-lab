# AGENTS.md

## Service Role

- `demo-order-service` 是一个最小 Spring 风格服务模板
- 目标是演示微服务仓库如何内置 Harness 基础能力
- 这里重点展示分层结构、契约目录、ArchUnit 测试，而不是完整业务功能

## Project Map

- `pom.xml`：Maven 构建与测试依赖
- `src/main/java/com/example/order/controller`：接口层
- `src/main/java/com/example/order/service`：业务层
- `src/main/java/com/example/order/domain`：领域模型
- `src/main/java/com/example/order/repository`：持久化接口
- `src/test/java/com/example/order/architecture`：架构约束测试
- `src/test/java/com/example/order/service`：业务层测试
- `contracts/`：接口或事件契约样例

Start here:

- 看结构先读 `README.md`
- 看分层约束先读 `src/test/java/com/example/order/architecture/LayeredArchitectureTest.java`
- 看接口契约先读 `contracts/openapi-order.yaml`

## Working Rules

- 保持标准分层：controller -> service -> repository
- 不要跨层直接访问内部实现
- 契约变更必须同步更新 `contracts/`
- 小步修改，不做无关重构

## Hard Constraints

- Controller 不写业务规则
- Domain 不依赖 controller
- 不要删除 ArchUnit 测试
- 不要修改公共契约而不更新契约文件

## Verification

- `mvn test`

## Escalation

以下情况先确认：

- 修改契约文件结构
- 修改分层规则
- 新增跨服务调用

