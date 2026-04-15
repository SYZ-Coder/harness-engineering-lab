# 实验 02：构建一个最小可运行的 Harness Demo

> 验证概念：AGENTS.md 入口设计、任务文件化、测试门控、最小验证闭环
> 复杂度：⭐

## 目标

构建一个尽可能小、但又具备 Harness Engineering 基本要素的示例项目：

- 人类通过 `PROMPT.md` 定义任务
- 通过 `AGENTS.md` 提供仓库导航与约束
- 智能体生成代码与测试
- 用测试作为最小背压门控

这个实验不追求复杂编排，而是展示：

> 即使没有多智能体、没有 session、没有平台化基础设施，Harness Engineering 也可以以极简形式落地。

## 目录结构

```text
practice/02-minimal-harness-demo/
├── AGENTS.md
├── PROMPT.md
├── README.md
├── sample_tasks.md
├── src/
│   └── todo_summary.py
└── tests/
    └── test_todo_summary.py
```

## 这个 Demo 展示了什么

### 1. 仓库即记录系统

任务、约束、输入样例、测试全部在仓库里。  
智能体不需要依赖聊天窗口里的“隐性上下文”。

### 2. 地图而非手册

`AGENTS.md` 很短，但回答了最重要的问题：

- 先看什么
- 哪些不能碰
- 运行什么验证

### 3. 机械化执行

通过 `python -m unittest` 形成最小门控。  
不是靠“我觉得写完了”，而是靠测试通过。

### 4. 人类掌舵，智能体执行

人类定义任务与边界；  
智能体负责实现和修复；  
验证信号决定能否继续。

## 如何使用这个 Demo

### 1. 阅读入口文件

先看：

- `AGENTS.md`
- `PROMPT.md`

### 2. 运行测试

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### 3. 运行示例

```bash
python src/todo_summary.py sample_tasks.md
```

预期输出示例：

```text
File: sample_tasks.md
Total: 4
Open: 2
Done: 2
```

## 这个 Demo 为什么有价值

很多人会误以为 Harness Engineering 必须从重型架构开始，例如：

- 多智能体
- 长时 session
- 自动化评估平台
- managed agents

但实际上，大多数团队更需要的第一步是：

- 一个清楚的入口
- 一个文件化任务
- 一套最小验证命令
- 一个可以复用的“人类掌舵”样板

这个 Demo 的价值就在于把这些最小元素具体化。

## 下一步如何扩展

如果要把这个 Demo 从最小版升级，可以继续加：

1. 一个简单的 `Makefile` 或脚本入口
2. 针对输出格式的结构测试
3. 针对错误信息的更细粒度断言
4. 一份 `DECISIONS.md` 记录设计权衡
5. 一个二阶段循环：先实现，再独立 review

## 对应到原创专题的阅读顺序

- 想先理解整体：看 `works/harness-engineering-how-to-use-and-land.md`
- 想理解入口文件：看 `works/mvp-agents-template-for-small-teams.md`
- 想理解验证设计：看 `works/harness-validation-loop.md`
- 想理解实施顺序：看 `works/harness-implementation-roadmap-for-teams.md`

