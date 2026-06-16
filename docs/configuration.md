# ⚙️ 配置说明

## 配置文件结构

复制模板后编辑：

```bash
cp templates/evol_config.yaml config.yaml
```

## 配置项详解

### 基础配置

```yaml
project:
  name: "hermes-self-evolution"
  version: "0.1.0"
  data_dir: "./data"
  log_dir: "./logs"
  report_dir: "./reports"
```

### 模型配置

```yaml
model:
  provider: "openai"          # openai | anthropic | vllm | local
  api_key: "${OPENAI_API_KEY}" # 支持环境变量引用
  base_url: "https://api.openai.com/v1"
  model_name: "gpt-4o-mini"   # 或 "claude-3-haiku" / "hermes-3-llama-3.1-8b"
  temperature: 0.7
  max_tokens: 4096
```

### 评分配置

```yaml
scoring:
  weights:
    correctness: 0.40
    completeness: 0.25
    readability: 0.20
    safety: 0.15
  judge_model: "gpt-4o"       # 评判模型（通常用更强的模型）
```

### 进化配置

```yaml
evolution:
  candidates_per_round: 5     # 每轮候选数
  top_k: 3                    # 保留 Top-K
  max_iterations: 20          # 最大迭代轮数
  convergence_threshold: 0.5  # 连续 N 轮提升小于此值则停止
```

### 记忆配置

```yaml
memory:
  backend: "sqlite"           # sqlite | postgresql
  sqlite_path: "data/evolution.db"
  retention_days: 90
```

## 环境变量

| 变量名 | 说明 | 必填 |
|--------|------|------|
| `OPENAI_API_KEY` | OpenAI API 密钥 | 依赖 provider |
| `ANTHROPIC_API_KEY` | Anthropic API 密钥 | 依赖 provider |
| `EVOL_DB_URL` | 数据库连接 URL | 仅 PostgreSQL |
