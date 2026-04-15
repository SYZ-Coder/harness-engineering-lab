# 实验 03：Spring 微服务模板 Demo

> 验证概念：分层约束、契约文件、仓库入口、最小微服务 Harness
> 复杂度：⭐⭐

## 目标

这个 Demo 不是完整的业务系统，而是一个“可复制的微服务仓库样板”。

它展示的是：一个 Spring Cloud / Java 微服务仓库，如果想对智能体更友好，最少应该内置什么。

包括：

- 一个面向智能体的 `AGENTS.md`
- 清晰的 controller / service / domain / repository 分层
- 一个最小的契约文件目录 `contracts/`
- 一个 ArchUnit 测试，机械化约束层次边界
- 一个业务层测试，验证核心行为
- 一个 `otel/README.md`，展示最小 OpenTelemetry 接入骨架

## 目录结构

```text
practice/03-spring-service-template-demo/
├── AGENTS.md
├── README.md
├── pom.xml
├── otel/
│   └── README.md
├── contracts/
│   └── openapi-order.yaml
└── src/
    ├── main/java/com/example/order/
    │   ├── controller/OrderController.java
    │   ├── domain/Order.java
    │   ├── repository/OrderRepository.java
    │   └── service/OrderService.java
    └── test/java/com/example/order/
        ├── architecture/LayeredArchitectureTest.java
        └── service/OrderServiceTest.java
```

## 这个 Demo 展示了什么

### 1. 微服务入口层

`AGENTS.md` 告诉智能体：

- 这个服务负责什么
- 仓库怎么导航
- 哪些边界不能碰
- 最少运行什么验证

### 2. 结构性约束

`LayeredArchitectureTest` 用 ArchUnit 把：

- controller 只能访问 service
- service 只能访问 repository / domain

这种规则编码为测试。

### 3. 契约前置

`contracts/openapi-order.yaml` 展示了：

- 公共接口不应只存在于代码里
- 接口演进应有一个稳定事实来源

### 4. 可观测性骨架

`otel/README.md` 展示了：

- 怎么给服务声明稳定的 `service.name`
- 怎么为 OTLP exporter 预留配置
- 怎么把可观测性作为 Harness 的运行时反馈层接入

### 5. 最小业务测试

`OrderServiceTest` 说明：

- 不只是要有结构规则
- 也要有针对核心行为的最小验证

## 如何使用

### 1. 阅读入口

先看：

- `AGENTS.md`
- `contracts/openapi-order.yaml`

### 2. 运行测试

```bash
mvn test
```

### 3. 看这个样板如何迁移到真实仓库

可以把这个 Demo 理解成一个“最小起点”，真实项目中通常还会继续加：

- Spring Boot application
- OpenAPI 生成或 contract verification
- OpenTelemetry 配置
- 数据库迁移脚本
- CI 骨架

## 为什么它适合重型微服务团队

因为很多团队一开始并不缺“更复杂的平台”，而是缺一个统一的、能复制的最小样板。

这个 Demo 的价值就在于把以下三件事捆在一起：

- 入口
- 约束
- 契约
- 运行时反馈入口

让微服务仓库从第一天起就更容易被 Harness。

