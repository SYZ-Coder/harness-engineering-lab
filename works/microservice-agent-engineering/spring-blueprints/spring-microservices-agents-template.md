# Spring Cloud / Java 微服务 AGENTS.md 模板

> 面向这样一种仓库：  
> 服务是 Java / Spring Boot / Spring Cloud 技术栈，位于一个更大的微服务体系中。  
> 目标不是写一份“万能规范大全”，而是给编码智能体一张足够清晰、足够短、足够可执行的入口地图。

---

## 一、先说结论：微服务仓库的 AGENTS.md，重点不是“把所有规范都写进去”，而是让智能体快速回答 4 个问题

对一个 Spring 微服务仓库来说，智能体最先需要知道的，通常不是全部代码规范，而是：

1. 这个服务在整个系统里负责什么
2. 这个仓库应该从哪里开始读
3. 哪些层和边界不能越过
4. 做完后至少要跑哪些验证

因此，一个好的微服务 `AGENTS.md`，应该优先服务于：

- 仓库导航
- 服务定位
- 风险边界
- 最小验证链

而不是试图自己承担全部架构文档和团队知识库的职责。

---

## 二、微服务版 AGENTS.md 最少应包含什么

## 1. 服务定位

至少写清：

- 这是哪个服务
- 主要职责是什么
- 它依赖哪些上游 / 下游系统
- 它暴露 HTTP API、消息消费，还是定时任务

为什么重要：

因为在微服务里，最常见的问题不是“怎么写这个方法”，而是：

> 这个需求到底该不该在这个服务里实现。

## 2. 仓库地图

至少写清：

- controller / api 在哪
- service 在哪
- domain 在哪
- repository / persistence 在哪
- config、integration、contract、test 在哪

为什么重要：

因为 Spring 微服务天然分层，智能体需要快速知道“每一层的代码应该去哪看、去哪改”。

## 3. 硬边界

至少写清：

- Controller 不写业务逻辑
- Service 不直接耦合外部实现细节
- 不允许跨模块访问内部包
- 不允许跳过契约层直接“猜接口”

为什么重要：

这类规则是智能体最容易破坏、也是最贵的错误来源。

## 4. 最小验证

至少写清：

- `mvn test`
- 需要运行的 contract test / ArchUnit test
- 涉及接口变更时要检查什么

为什么重要：

没有验证说明，智能体极容易“能编译就算完成”。

## 5. 风险升级条件

至少写清：

- 改数据库 schema 先停
- 改 OpenAPI / DTO / 事件结构先停
- 改鉴权、支付、配置中心、网关规则先停

为什么重要：

微服务里很多问题不是代码层的，而是系统层的高风险变更。

---

## 三、推荐结构

下面这套结构，适合大多数 Spring Boot 微服务仓库。

```md
# AGENTS.md

## Service Role

- This service owns ...
- It exposes ...
- It depends on ...

## Project Map

- `src/main/java/.../controller`：HTTP 接口层
- `src/main/java/.../service`：业务逻辑层
- `src/main/java/.../domain`：领域模型
- `src/main/java/.../repository`：持久化层
- `src/test/java`：测试
- `src/main/resources`：配置

Start here:

- 改接口先看 OpenAPI / controller / contract tests
- 改业务规则先看 service / domain / tests
- 改持久化先看 repository / migration / integration tests

## Working Rules

- 小步修改，避免无关重构
- 优先复用现有模式
- 有测试先读测试
- 不要猜测跨服务契约

## Hard Constraints

- Controller 不写业务逻辑
- 不要跨模块访问内部包
- 不要绕过 service 层直接访问 persistence
- 不要修改公共契约而不更新 contract tests / docs

## Verification

- `mvn test`
- `mvn -Dtest=*ArchUnit* test`
- 如改接口：运行契约相关测试

## Escalation

以下情况先确认：

- 数据库 schema 变更
- OpenAPI / DTO / 事件结构变更
- 鉴权、支付、网关、配置中心相关变更
- 跨服务调用方式调整
```

---

## 四、一个更贴近 Spring Cloud 的成品模板

下面给一份更贴近真实团队的版本。

```md
# AGENTS.md

## Service Role

- `order-service` 负责订单创建、状态流转和订单查询
- 对外暴露 REST API
- 消费 `payment-confirmed` 事件
- 依赖 `inventory-service` 与 `payment-service`

## Project Map

- `src/main/java/com/example/order/controller`：REST controllers
- `src/main/java/com/example/order/service`：application services
- `src/main/java/com/example/order/domain`：domain objects and rules
- `src/main/java/com/example/order/repository`：persistence adapters
- `src/main/java/com/example/order/integration`：remote client / messaging adapters
- `src/test/java`：unit / integration / contract / architecture tests
- `src/main/resources/db/migration`：database migrations

Start here:

- 改 REST 接口：先看 controller、DTO、OpenAPI、contract tests
- 改领域逻辑：先看 domain、service、对应测试
- 改远程调用：先看 integration、clients、契约与回归测试
- 改数据库：先看 migration、repository、integration tests

## Working Rules

- 优先保持既有分层与命名风格
- 小步修改，只动与当前需求直接相关的代码
- 优先复用现有 client、mapper、exception handling 模式
- 如果测试已表达期望，先对齐测试再修改实现

## Hard Constraints

- Controller 不承载业务规则
- Domain 不依赖 web/controller 层
- 不要跨模块直接访问内部实现
- 不要修改公共 DTO / event payload 而不更新契约说明与测试
- 不要跳过已有 client / gateway 直接拼接临时调用

## Verification

- `mvn test`
- 如改架构边界：运行 ArchUnit tests
- 如改公共接口：运行 contract tests
- 如改数据库：运行 repository / integration tests

## Escalation

以下情况先停下确认：

- 数据库 schema 或迁移脚本变更
- OpenAPI、公共 DTO、事件结构变更
- 鉴权、权限、支付、风控逻辑变更
- 新增或调整跨服务调用链
```

---

## 五、配套文件建议

为了让这个 `AGENTS.md` 真正有用，建议给 Spring 微服务至少配这些文件：

- `docs/service-overview.md`
- `docs/api-contract.md`
- `docs/dependencies.md`
- `src/test/java/.../ArchUnit...`
- OpenAPI 或契约测试骨架

原则是：

> `AGENTS.md` 做入口，细节放到专门文档和测试里。

---

## 六、在微服务里最容易写错的地方

## 错误 1：只写仓库结构，不写服务职责

结果：

- 智能体知道“去哪改”
- 但不知道“该不该在这儿改”

## 错误 2：只写建议，不写硬边界

结果：

- 所有规则看起来一样轻
- 最关键的架构约束没有被凸显

## 错误 3：不写契约和跨服务风险

结果：

- 智能体把微服务当成单仓库应用来处理
- 很容易只改本地代码，不管外部兼容性

## 错误 4：验证命令不具体

结果：

- 智能体跑了最容易跑的命令
- 没跑最该跑的测试

---

## 七、最小落地建议

如果你要在现有 Spring Cloud 系统里批量补 `AGENTS.md`，建议这样做：

1. 先挑一类最典型的服务
2. 提炼一份模板
3. 每个仓库只保留 40 到 80 行
4. 把详细内容链接到文档和测试
5. 每次复盘失败样本时回写模板

这会比“每个服务自由发挥”稳定得多。

---

## 总结

Spring 微服务仓库里的 `AGENTS.md`，本质上应该回答的是：

- 这个服务在系统里负责什么
- 这个仓库该从哪里开始读
- 哪些边界绝对不能碰
- 做完后最少要跑什么验证

做到这四点，它就已经不只是普通说明文件，而是微服务 Harness 的入口层。

