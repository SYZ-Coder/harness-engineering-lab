# 微服务团队落地 Harness Engineering 全景指南

> 面向这样一种团队：  
> 系统已经是微服务架构，服务很多、链路很长、历史包袱很重，大家已经开始用 AI 写代码，但逐渐发现问题不在“会不会生成”，而在“怎样让它稳定地嵌进现有系统”。

这篇文章试图给出一个更完整的答案：

> **微服务里的 Harness Engineering，不是先造更强的智能体，而是先让系统对智能体可读、可约束、可验证、可诊断、可复制。**

---

## 一、微服务为什么会放大 AI 使用中的所有问题

在单仓库、单应用场景里，AI 的问题常常表现为：

- 生成风格不稳定
- 测试遗漏
- 设计有点飘

但在微服务里，这些问题会被系统复杂度成倍放大。

同样一个需求，往往意味着：

- 改多个服务
- 看多个 API 契约
- 处理多个 owner 和边界
- 验证多条链路
- 观察运行时联动

这就导致一个关键现实：

> 微服务里最难的已经不是“写出某段代码”，而是“在正确的服务、正确的边界、正确的兼容性约束、正确的运行信号下写那段代码”。

所以微服务落地 Harness Engineering，重点一定是系统工程，而不是单次对话技巧。

---

## 二、微服务 Harness 的 5 层结构

如果把微服务里的 Harness 抽象成一个系统，我建议按下面 5 层来理解。

## 1. 入口层

解决：

- 服务太多，不知道从哪儿开始

典型组件：

- Backstage Catalog
- TechDocs
- 仓库级 `AGENTS.md`

## 2. 约束层

解决：

- 架构边界容易被破坏

典型组件：

- ArchUnit
- 包依赖规则
- 服务模板

## 3. 验证层

解决：

- 改完后不知道是否破坏兼容性

典型组件：

- 单元测试
- 集成测试
- Spring Cloud Contract / Pact / Microcks

## 4. 反馈层

解决：

- 上线后出了问题看不清

典型组件：

- OpenTelemetry
- trace / logs / metrics
- 运行时诊断入口

## 5. 复制层

解决：

- 每个服务都在重复踩坑

典型组件：

- 服务模板
- OpenRewrite
- 标准化 CI 骨架

这 5 层不是理论划分，而是很适合指导实施顺序的工程分层。

---

## 三、最现实的落地顺序

如果你的系统很重，我建议按下面顺序推进。

### 阶段 1：先补入口

做什么：

- 给核心服务补 `AGENTS.md`
- 补服务职责和依赖说明
- 用 Backstage / 文档系统形成服务地图

### 阶段 2：再补结构约束

做什么：

- 加 ArchUnit
- 冻结存量违规
- 先守住新增违规

### 阶段 3：再补契约验证

做什么：

- 给关键调用链加 contract verification
- 固定接口事实来源

### 阶段 4：再补运行反馈

做什么：

- 接入 OpenTelemetry
- 打通 trace 和日志

### 阶段 5：最后做规模化复制

做什么：

- 服务模板
- OpenRewrite
- 平台化能力

---

## 四、一个可以快速嫁接的组合包

如果你现在就想给现有 Spring Cloud / Java 微服务体系加一层 Harness，我建议先做这个“最小组合包”：

### 每个服务至少有

- 一个简短 `AGENTS.md`
- 一个服务职责说明
- 一个契约文件入口
- 一组最小 ArchUnit 规则
- 一组基础业务测试

### 核心链路至少有

- 一条契约验证链
- 一条可追踪的 trace 链

### 团队层至少有

- 高风险变更升级条件
- 高频失败模式回写机制

---

## 五、建议怎么用本仓库里的材料

如果你想把这套方法直接落到 Spring 微服务团队，可以按这个顺序使用本仓库：

1. `works/harness-engineering-how-to-use-and-land.md`
2. `../../general-agent-engineering/adoption-guides-and-roadmaps/harness-engineering-how-to-use-and-land.md`
3. `spring-microservices-harness-blueprint.md`
4. `spring-microservices-agents-template.md`
5. `../contract-testing-playbooks/spring-microservices-contract-observability-playbook.md`
6. `../contract-testing-playbooks/spring-microservices-archunit-contract-checklist.md`
7. `../../../practice/03-spring-service-template-demo/`

---

## 六、最值得避免的 5 个误区

### 误区 1：先做多智能体，不先做服务地图

结果：

- 智能体更快地在错误服务里做更多错误改动

### 误区 2：只有代码生成，没有结构约束

结果：

- 生成速度提高了，架构质量下降得更快

### 误区 3：把契约问题留给联调

结果：

- 兼容性问题依旧在最贵的阶段才暴露

### 误区 4：有监控平台，但没有把它变成反馈层

结果：

- 可观测性只是大屏，不是 Harness 的信号来源

### 误区 5：一开始就想平台化

结果：

- 能力建得很多，但没有一条真正跑通的最小闭环

---

## 七、一个更实用的判断标准

判断微服务 Harness 做得好不好，不要只看：

- AI 写得快不快

更应该看：

- 智能体能否快速定位到正确服务
- 架构边界是否更稳了
- 接口兼容性问题是否更早暴露了
- 排障是否更快了
- 好实践是否能复制到更多服务

---

## 总结

微服务团队落地 Harness Engineering，最核心的变化不是工具升级，而是工程环境升级。

真正值得追求的目标不是：

- “让 AI 更会写代码”

而是：

- “让系统本身更适合被 AI 和团队共同驾驭”

当入口、约束、验证、反馈、复制这五层逐步接起来，微服务团队才会真正从“在复杂系统里试着用 AI”过渡到“在可治理系统里稳定使用 AI”。

