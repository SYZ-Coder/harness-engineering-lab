# 实验 09：最小验证闭环 Demo

> 验证概念：lint、测试、AI review、人工 review 的最小组合
> 复杂度：⭐⭐

## 目标

这个 Demo 展示的是 Harness Engineering 里最核心、也最容易被说空的一层：

> 验证闭环到底怎么拆，哪些问题该交给 lint，哪些交给测试，哪些需要 review。

这里我们用一个非常小的订单金额计算样例，把 4 层信号拆开：

- lint-style 校验
- 可执行测试
- AI review 清单
- 人工 review 清单

它不追求模拟完整 CI 平台，而是帮助读者看清：

- 每一层解决什么问题
- 每一层不能替代什么
- 为什么验证闭环必须是组合，而不是单点工具

## 目录结构

```text
practice/09-validation-review-demo/
├── AGENTS.md
├── README.md
├── src/
│   └── order_total.py
├── tools/
│   └── validate_demo.py
├── reviews/
│   ├── ai-review-checklist.md
│   └── human-review-checklist.md
└── tests/
    └── test_validation_review_demo.py
```

## 这个 Demo 展示了什么

### 1. lint-style 校验负责抓“明显不该出现的东西”

这里的 `tools/validate_demo.py` 不是完整 linter，  
但它模拟了最小的机械校验思路：

- 关键函数必须存在
- 不应该残留 `TODO`
- 不应该偷偷用负数折扣

它代表的是：

- 机械
- 前置
- 快速
- 不依赖人主观判断

### 2. 测试负责抓行为

`tests/test_validation_review_demo.py` 负责验证：

- 基本金额计算是否正确
- 折扣是否正确应用
- 异常输入是否被拒绝

它回答的是：

> 代码跑出来的行为，到底对不对。

### 3. AI review 更适合当“结构化第二视角”

AI review 清单不会替代测试，也不会替代人。

它更适合帮助你追问：

- 有没有隐藏的边界条件
- 命名和可读性是否会误导后续智能体
- 逻辑是否和 README / 规则一致

### 4. 人工 review 仍然要看风险和业务语义

人工 review 清单强调的是：

- 这个实现是否符合真实业务语义
- 是否会带来未来维护成本
- 是否值得合并

这部分往往最难自动化。

## 如何运行

```bash
python tools/validate_demo.py
python -m unittest discover -s tests -p "test_*.py"
```

## 适合映射到真实系统的地方

这个 Demo 对应到真实工程里，通常就是：

- lint / 静态规则
- unit tests / integration tests
- AI code review
- human PR review

真实系统会更复杂，但分层思路和这里是一样的：

> 不同验证手段解决不同类型的问题，不要把所有希望都压在某一个工具上。

## 为什么它适合放进 Harness 仓库

因为 Harness 的关键不只是“会不会生成代码”，而是：

> 生成后的结果，如何被不同层级的反馈信号拦住、验证、解释和放行。

这个 Demo 补的正是这层最小反馈回路。

