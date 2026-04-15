# 实验 07：最小 OpenRewrite Demo

> 验证概念：批量治理、确定性重写、field injection 到 constructor injection
> 复杂度：⭐⭐

## 目标

这个 Demo 展示的是微服务和 Spring 项目里另一类非常典型的工程落地点：

> 不是修一个 bug，而是把一类重复出现的代码形态批量改成团队想要的新标准。

这里我们用一个最常见的 Spring 改造例子来说明：

- 历史代码使用 field injection
- 团队希望统一改成 constructor injection
- 改造应该是可重复、可审查、可验证的

这个目录不会真的运行 OpenRewrite 引擎，而是用一个最小 Python 重写器把核心思想讲清楚：

- 规则先被定义
- 变更是确定性的
- before / after 可以被对照
- 测试可以保证这类改造不会悄悄漂移

## 目录结构

```text
practice/07-openrewrite-demo/
├── AGENTS.md
├── README.md
├── fixtures/
│   ├── before/
│   │   └── LegacyOrderService.java
│   └── after/
│       └── LegacyOrderService.java
├── recipes/
│   └── field-injection-to-constructor.md
├── src/
│   └── rewrite_demo.py
└── tests/
    └── test_rewrite_demo.py
```

## 这个 Demo 展示了什么

### 1. 批量治理的关键不是“写更多代码”，而是“表达一条稳定规则”

在真实项目里，很多技术债并不是单点问题，而是成百上千个类似写法：

- field injection
- 过时 API
- 旧版依赖
- 分层边界不一致

真正有价值的，不是手工修一处，而是把规则变成可重复执行的改造。

### 2. before / after 比口头规范更容易推广

这个 Demo 直接给了一对样板：

- `fixtures/before/LegacyOrderService.java`
- `fixtures/after/LegacyOrderService.java`

它让团队更容易看到：

- 旧写法长什么样
- 新写法长什么样
- 一条 recipe 到底会改什么

### 3. 确定性工具和 AI 是互补关系

在真实工程里，OpenRewrite 这类工具适合负责：

- 机械、重复、批量的一致性改造

而 AI 更适合负责：

- 解释为什么要改
- 帮团队评估风险
- 补文档、补测试、补迁移说明

### 4. 批量治理也需要验证闭环

这里的测试会验证：

- `@Autowired` 字段注入被移除
- 字段被改成 `private final`
- 构造函数被正确补出
- 最终结果与期望样板一致

## 如何运行

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 适合映射到真实系统的地方

这个 Demo 对应到真实 Spring / Java 微服务世界里，通常就是：

- 用 OpenRewrite 批量把 field injection 改成 constructor injection
- 批量升级 Spring Boot / Spring Cloud 版本
- 统一 API 写法
- 批量替换旧依赖或过时调用方式

在真实项目里，你通常会把这里的最小模式升级为：

- `rewrite.yml`
- `rewrite-maven-plugin`
- 官方 Spring recipes
- CI 中的 dryRun / review 流程

但它们背后的核心思想和这里是同一个：

> **把“靠人记忆的规范”升级成“可重复执行的改造规则”。**

## 为什么它适合放进 Harness 仓库

因为在工程化落地里，除了入口、验证、契约、可观测性之外，还有一层经常被忽略：

- 历史系统如何低风险、批量地往目标形态演进

`practice/05-contract-testing-demo/` 解决变更前兼容性，  
`practice/06-observability-demo/` 解决变更后运行反馈，  
这个 Demo 解决的是：

> 如何把一类历史写法系统性地改到团队期望的目标样式。

