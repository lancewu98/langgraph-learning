# Python LangGraph 项目

这个项目展示了如何使用 LangGraph 框架结合阿里云百炼平台的大模型进行开发。

## 环境要求

- Python 3.8+
- pip

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

复制 `.env.example`（如果有的话）为 `.env`，并填入你的配置：

```bash
cp .env.example .env
# 然后编辑 .env 文件，填入你的 API key 等信息
```

或者直接创建 `.env` 文件：

```env
OPENAI_API_KEY=你的API_KEY
OPENAI_BASE_URL=https://ws-hf6rt8uqd1bygr11.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
MODEL_NAME=qwen3.7-plus
```

### 5. 运行项目

```bash
# 运行基础示例
python test4_model.py

# 运行对话记忆示例
python test5_memory.py

# 运行流式输出示例
python test6_streamOutput.py
```

## 项目文件说明

| 文件 | 说明 |
|------|------|
| `test1_simple.py` | 最简单的 LangGraph 示例 |
| `test2_if.py` | 条件判断示例 |
| `test3_for.py` | 循环示例 |
| `test4_model.py` | 集成 LLM 的基础示例 |
| `test5_memory.py` | 带有对话记忆的示例 |
| `test6_streamOutput.py` | 流式输出示例 |
| `.env` | 环境变量配置（不提交到 git） |
| `requirements.txt` | 项目依赖列表 |

## 注意事项

1. 不要将 `.env` 文件提交到 git（已在 `.gitignore` 中配置）
2. 确保 API key 有足够的配额
3. 推荐使用虚拟环境进行开发

## 技术栈

- LangGraph - 用于构建有状态的多角色应用
- LangChain - LLM 应用开发框架
- Pydantic - 数据验证
- Python-dotenv - 环境变量管理
