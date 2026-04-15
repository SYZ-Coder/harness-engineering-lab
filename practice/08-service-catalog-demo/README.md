# 实验 08：最小服务目录 Demo

> 验证概念：服务目录、自描述元数据、owner/依赖/API 入口、平台映射
> 复杂度：⭐⭐

## 目标

这个 Demo 展示的是微服务工程化里另一类非常典型、但经常被忽略的落地点：

> 服务很多时，团队和智能体能不能快速知道“这个服务是谁负责、做什么、依赖谁、暴露什么 API、属于哪个系统”。

这里我们采用“双层服务目录样板”：

- 一层是平台导向的 `catalog-info.yaml`
- 一层是仓库内自描述的 `service.yaml`

这样做的好处是：

- 可以映射到 Backstage 一类平台
- 即使没有平台，这个仓库本身也仍然可读
- 人和智能体都能用同一套入口快速理解服务

## 目录结构

```text
practice/08-service-catalog-demo/
├── AGENTS.md
├── README.md
├── catalog-info.yaml
├── service.yaml
├── ownership/
│   └── owner.md
├── apis/
│   └── openapi-order-query.yaml
├── dependencies/
│   └── services.yaml
├── docs/
│   └── service-overview.md
└── tests/
    └── test_catalog_demo.py
```

## 这个 Demo 展示了什么

### 1. 平台目录和仓库目录不是二选一

真实团队里，服务目录经常有两种需求：

- 平台要能收集元数据
- 仓库自己也要能自解释

所以这里同时保留：

- `catalog-info.yaml`
- `service.yaml`

前者更适合平台收录，后者更适合仓库内阅读、自动化和智能体理解。

### 2. 一个服务至少要能回答几个基本问题

这个样板里的 `order-query-service` 会明确回答：

- 这个服务属于哪个系统
- 谁是 owner
- 暴露什么 API
- 依赖哪些上游或下游服务
- 出问题时先看哪里

### 3. 服务目录不是“介绍页”，而是工程入口

这个 Demo 的重点不是写漂亮文档，而是让目录信息变成工程中的真实入口：

- `catalog-info.yaml` 供平台发现
- `service.yaml` 供仓库内自动化使用
- `apis/` 提供接口入口
- `dependencies/` 提供依赖入口
- `ownership/` 提供责任入口

### 4. 元数据也需要验证

服务目录如果不校验，很快就会漂移。

这里的测试会做最小强度的关键字段存在与对齐检查：

- 平台元数据和仓库元数据中的关键名称、owner、system 等文本对齐
- owner、system、lifecycle、api 引用等关键字段存在
- 依赖清单完整

## 如何运行

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 适合映射到真实系统的地方

这个 Demo 对应到真实微服务世界里，通常就是：

- `catalog-info.yaml` 接入 Backstage Catalog
- `service.yaml` 作为仓库入口文件之一
- `apis/` 里的 OpenAPI 文件供 API portal 或智能体读取
- `dependencies/` 帮助人和自动化理解调用链
- `ownership/` 让值班、治理和升级路径更清楚

## 为什么它适合放进 Harness 仓库

因为微服务 Harness 不只是：

- 有规则
- 有验证
- 有契约
- 有可观测性

它还需要先回答：

> 智能体和人到底能不能快速“看懂系统里有哪些服务，以及每个服务的责任和边界”。

这个 Demo 补的正是这层“可读性基础设施”。


