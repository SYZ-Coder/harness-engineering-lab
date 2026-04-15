# AGENTS.md

## Project Map

- `src/todo_summary.py`：CLI 主程序与核心统计逻辑
- `tests/test_todo_summary.py`：单元测试
- `sample_tasks.md`：示例输入文件
- `PROMPT.md`：交给智能体的任务描述

Start here:

- 改功能前先看 `PROMPT.md`
- 改逻辑前先看 `tests/test_todo_summary.py`
- 改输出格式前先看 `sample_tasks.md`

## Working Rules

- 优先保持标准库实现，不引入第三方依赖
- 先复用现有函数，再新增函数
- 小步修改，避免无关重构
- 输出保持可读，错误信息要明确

## Hard Constraints

- 不要引入外部包
- 不要修改任务范围之外的功能
- 不要跳过测试直接宣布完成
- 不要把解析逻辑写成难以测试的脚本堆叠

## Verification

- `python -m unittest discover -s tests -p "test_*.py"`

## Escalation

以下情况先停下确认：

- 修改输入文件格式约定
- 删除测试
- 改 CLI 参数语义

