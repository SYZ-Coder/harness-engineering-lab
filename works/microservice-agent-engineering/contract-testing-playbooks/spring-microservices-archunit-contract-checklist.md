# Spring 微服务 ArchUnit + 契约检查清单

> 面向这样的问题：  
> 团队已经决定在 Spring 微服务里引入结构约束和契约测试，但落地时常常会变成“概念上都同意，实施时不知道先检查什么”。  
> 这份清单的目标，就是把最值得优先落地的检查项压缩成一页。

---

## 一、仓库入口

- [ ] 服务仓库有 `AGENTS.md`
- [ ] `AGENTS.md` 写清服务职责、依赖、风险升级条件
- [ ] 仓库说明了契约文件存放位置
- [ ] 仓库说明了 ArchUnit / contract test 的运行方式

---

## 二、ArchUnit 结构约束

- [ ] 已定义 controller / service / repository / domain 基本分层
- [ ] Controller 不直接访问 persistence
- [ ] Service 不依赖 web 层
- [ ] Domain 不依赖 controller
- [ ] 已检查循环依赖或模块越界
- [ ] 遗留系统采用 freeze 或等价策略控制新增违规

如果这几项都没有，微服务的结构会非常容易在智能体高吞吐改动下持续腐坏。

---

## 三、契约事实来源

- [ ] 至少一个公开接口有 OpenAPI / AsyncAPI / contract 文件
- [ ] 团队明确了谁维护契约
- [ ] Provider 变更会触发契约相关验证
- [ ] Consumer 依赖已被识别
- [ ] 公共 DTO / event payload 变更不再只靠口头同步

---

## 四、CI 与验证

- [ ] `mvn test` 包含基础业务测试
- [ ] ArchUnit 测试已纳入测试流程
- [ ] 契约相关测试或 verification 已纳入 CI
- [ ] 改接口时不会只跑本地单测就合并
- [ ] 团队知道哪些检查是硬门控，哪些只是提示信号

---

## 五、升级条件

- [ ] 修改 OpenAPI / DTO / event payload 会触发额外检查
- [ ] 修改跨服务调用链会触发 review
- [ ] 数据库 schema 变更不会绕过人工确认
- [ ] 高风险链路（鉴权、支付、库存、订单）有额外门控

---

## 六、最小落地判断

如果下面 4 项已经具备：

- 有 `AGENTS.md`
- 有 1 组 ArchUnit 规则
- 有 1 条关键链路的契约验证
- 有 CI 中的基本门控

那么你已经具备 Spring 微服务 Harness 的最小骨架。

如果还没有这些项，最优先做的通常不是“上更复杂的智能体平台”，而是先把这些基础约束接起来。

---

## 七、推荐配套阅读

- [Spring Cloud / Java 微服务 Harness 落地蓝图](../spring-blueprints/spring-microservices-harness-blueprint.md)
- [Spring 微服务 AGENTS.md 模板](../spring-blueprints/spring-microservices-agents-template.md)
- [Spring 微服务契约测试与可观测性 Playbook](spring-microservices-contract-observability-playbook.md)

---

## 总结

对 Spring 微服务来说，ArchUnit 和契约测试最有价值的地方在于：

- 一个守结构
- 一个守兼容性

把这两者接进仓库、测试和 CI 后，微服务系统才真正开始变得：

> **对智能体可约束、对团队可验证。**

