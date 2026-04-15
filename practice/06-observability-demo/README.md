# 实验 06：最小可观测性 Demo

> 验证概念：trace id 贯通、日志关联、跨服务请求链路
> 复杂度：⭐⭐

## 目标

这个 Demo 展示微服务里另一类非常典型的工程落地点：

> 系统上线后，出了问题能不能快速看清请求经过了哪些服务、用了哪个 trace id、在哪一步出错。

它不追求搭建完整的 OpenTelemetry 平台，而是用最小 Python 示例把最核心的思想讲清楚：

- 一个请求进入入口服务
- trace id 被创建或透传
- 下游服务接收同一个 trace id
- 所有日志都能按 trace id 串起来

## 目录结构

```text
practice/06-observability-demo/
├── AGENTS.md
├── README.md
├── services/
│   ├── gateway_service.py
│   └── order_service.py
├── shared/
│   └── tracing.py
└── tests/
    └── test_observability_demo.py
```

## 这个 Demo 展示了什么

### 1. trace id 是跨服务链路的最小公共线索

在真实微服务系统里，你不一定一开始就有完整指标、span、dashboard，  
但至少应该先做到：

- 每个请求都有 trace id
- trace id 可以跨服务传递
- 日志里能看到 trace id

### 2. 入口服务负责创建或透传 trace id

`gateway_service.py` 模拟入口服务：

- 如果上游没有传 trace id，就新建一个
- 如果上游已传，就继续沿用

### 3. 下游服务不重新发明 trace id

`order_service.py` 模拟业务服务：

- 接收 trace id
- 在日志里打印 trace id
- 返回结果时保留 trace id

### 4. 日志关联比“多打日志”更重要

这个 Demo 强调的不是日志数量，而是：

> **日志是否共享一个可追踪的上下文键。**

在这里，这个键就是 `trace_id`。

## 如何运行

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 适合映射到真实系统的地方

这个 Demo 对应到真实 Spring / Java 微服务世界里，通常就是：

- 网关 / BFF 生成或透传 trace context
- 服务内日志带 trace id
- OpenTelemetry / logging 系统把这些关联起来

它是完整可观测性体系最小但最关键的一步。

## 为什么它适合放进 Harness 仓库

因为在微服务 Harness 里，反馈层至少要有两种信号：

- 上线前：契约验证
- 上线后：运行时可观测信号

`practice/05-contract-testing-demo/` 解决前者，  
这个 Demo 解决后者。

把这两个样板放在一起，读者会更容易理解：

> 微服务 Harness 不只是写规则，更是让系统能在变更前后都提供可信反馈。

