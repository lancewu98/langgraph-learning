# Python LangGraph 项目

这个项目展示了如何使用 LangGraph 框架结合阿里云百炼平台的大模型进行开发，并集成 LangSmith 进行追踪。

## 环境要求

- Python 3.8+
- pip

## 项目结构

```
langgraph-learning/
├── .env.example        # 环境变量模板
├── .gitignore          # Git 忽略文件配置
├── README.md           # 项目说明文档
├── requirements.txt    # 项目依赖列表
└── src/                # 源码目录
    ├── test1_simple.py      # 最简单的 LangGraph 示例
    ├── test2_if.py          # 条件判断示例
    ├── test3_for.py         # 循环示例
    ├── test4_model.py       # 集成 LLM 的基础示例
    ├── test5_memory.py      # 带有对话记忆的示例
    └── test6_streamOutput.py # 流式输出示例
```

## 快速开始

### 1. 克隆或下载项目

### 2. 创建并激活虚拟环境

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Windows (Cmd)
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

复制 `.env.example` 为 `.env`，并填入你的配置：

```bash
cp .env.example .env
# 然后编辑 .env 文件，填入你的 API key 等信息
```

**完整的环境变量说明：**

| 变量 | 说明 | 是否必填 |
|------|------|----------|
| `OPENAI_API_KEY` | 阿里云百炼平台的 API Key | 是 |
| `OPENAI_BASE_URL` | OpenAI 兼容的 API 地址 | 是 |
| `MODEL_NAME` | 使用的模型名称（如 qwen3.7-plus） | 是 |
| `LANGSMITH_TRACING` | 是否启用 LangSmith 追踪（true/false） | 否 |
| `LANGSMITH_ENDPOINT` | LangSmith API 地址 | 否 |
| `LANGSMITH_API_KEY` | LangSmith API Key | 否 |
| `LANGSMITH_PROJECT` | LangSmith 项目名称 | 否 |

### 5. 运行项目

```bash
# 运行基础示例
python src/test4_model.py

# 运行对话记忆示例
python src/test5_memory.py

# 运行流式输出示例
python src/test6_streamOutput.py
```

## LangSmith 配置（可选）

LangSmith 可以帮助你调试、测试和监控你的 LangChain 应用。

1. 在 [LangSmith 官网](https://smith.langchain.com) 注册账号
2. 创建 API Key
3. 在 `.env` 文件中配置相关变量
4. 设置 `LANGSMITH_TRACING=true` 即可启用追踪

## 项目文件说明

| 文件 | 说明 |
|------|------|
| `src/test1_simple.py` | 最简单的 LangGraph 示例 |
| `src/test2_if.py` | 条件判断示例 |
| `src/test3_for.py` | 循环示例 |
| `src/test4_model.py` | 集成 LLM 的基础示例 |
| `src/test5_memory.py` | 带有对话记忆的示例 |
| `src/test6_streamOutput.py` | 流式输出示例 |
| `.env` | 环境变量配置（不提交到 git） |
| `.env.example` | 环境变量模板 |
| `requirements.txt` | 项目依赖列表 |

## 注意事项

1. 不要将 `.env` 文件提交到 git（已在 `.gitignore` 中配置）
2. 确保 API key 有足够的配额
3. 推荐使用虚拟环境进行开发
4. 如果使用 LangSmith，请确保 API Key 配置正确

## 技术栈

- LangGraph - 用于构建有状态的多角色应用
- LangChain - LLM 应用开发框架
- LangSmith - 调试、测试和监控 LangChain 应用
- Pydantic - 数据验证
- Python-dotenv - 环境变量管理
