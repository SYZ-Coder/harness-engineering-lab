# 实验 05：最小契约测试 Demo

> 验证概念：契约前移、provider verification、consumer 兼容性检查
> 复杂度：⭐⭐

## 目标

这个 Demo 用最小形式展示微服务里最典型的一类工程落地问题：

> provider 改了响应结构，本地代码可能还跑得通，但 consumer 很可能已经不兼容。

这个目录通过一个简单的订单查询例子展示：

- 契约文件作为事实来源
- provider 输出必须满足契约
- consumer 解析逻辑依赖契约字段
- 测试要能在联调前发现破坏性变更

## 目录结构

```text
practice/05-contract-testing-demo/
├── AGENTS.md
├── README.md
├── contracts/
│   └── order-response-contract.json
├── consumer/
│   └── order_client.py
├── provider/
│   └── order_provider.py
└── tests/
    └── test_contract_demo.py
```

## 这个 Demo 展示了什么

### 1. 契约文件是事实来源

`contracts/order-response-contract.json` 定义了：

- 请求方式
- 路径
- 响应状态码
- 响应体必须包含的字段

### 2. Provider 不是“自己觉得没问题”就算通过

`provider/order_provider.py` 负责返回数据，  
但真正的通过标准不是 provider 自评，而是：

- 是否满足契约

### 3. Consumer 依赖的是契约，不是 provider 的临时实现细节

`consumer/order_client.py` 说明：

- consumer 只认约定好的字段
- 如果 provider 少字段或改字段，解析会失败

### 4. 契约测试是联调前移

`tests/test_contract_demo.py` 做了三类验证：

- provider 当前实现满足契约
- consumer 能正确消费满足契约的数据
- 一个破坏性响应会被检测出来

## 如何运行

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 适合映射到真实微服务的场景

这个最小 Demo 对应真实系统里常见的几类链路：

- `order-service -> payment-service`
- `gateway -> customer-service`
- `inventory-service -> stock-service`

在真实项目里，你通常会把这里的最小模式升级为：

- OpenAPI
- Spring Cloud Contract
- Pact
- Microcks
- provider verification in CI

但它们解决的核心问题和这里是同一个：

> **把服务兼容性问题，从联调阶段前移到验证阶段。**

## 这个 Demo 为什么值得加进 Harness 仓库

因为在微服务体系里，最典型、最有工程价值的一类落地组合就是：

- 仓库入口
- 架构边界
- 契约验证
- 可观测性反馈

而契约测试正好是其中最容易做成“小而完整样板”的一层。

