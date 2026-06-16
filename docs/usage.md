# 📖 使用指南

## 快速上手

### 1. 单次进化

```bash
# 对指定问题进行进化
python scripts/evolve_once.py --prompt "请用通俗的语言解释神经网络"
```

### 2. 查看报告

```bash
python scripts/view_report.py --latest
```

输出示例：

```
📊 进化报告 (2025-06-16 02:00:03)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🆔 Round: 12 | Prompt: "解释神经网络"
📈 Top Score: 82.3  (较基线提升 +12.1%)
📋 评分详情:
   ✅ 正确性:   85.0
   📋 完整性:   79.5
   📖 可读性:   81.2
   🛡️ 安全性:   83.5
```

### 3. 持续进化（cron）

```bash
# 一键安装 cron 任务
python scripts/install_cron.py \
    --config config.yaml \
    --schedule "0 */6 * * *" \
    --log-dir ./logs
```

### 4. Python API 方式

```python
from hermes_evol import EvolutionPipeline

pipeline = EvolutionPipeline(config="config.yaml")

# 单次进化
result = pipeline.evolve("什么是强化学习？")
print(f"最佳回答评分: {result.top_score}")

# 批量进化
prompts = ["解释梯度下降", "什么是 Transformer"]
results = pipeline.evolve_batch(prompts)

# 查看历史
history = pipeline.get_history(limit=10)
```

## 进阶用法

### 自定义评分规则

在 `config.yaml` 中添加自定义评分维度：

```yaml
scoring:
  custom_metrics:
    - name: "creativity"
      prompt: "评估答案的创意程度 (0-100)"
      weight: 0.1
```

### 多模型协同

```yaml
model:
  generators:
    - provider: "openai"
      model: "gpt-4o-mini"
      weight: 0.5
    - provider: "anthropic"
      model: "claude-3-haiku"
      weight: 0.3
    - provider: "vllm"
      model: "hermes-3-llama-3.1-8b"
      weight: 0.2
```

### 回滚机制

当进化评分连续下降时，自动回滚：

```bash
python scripts/evolve_once.py --rollback-threshold 3
# 连续 3 轮评分下降则自动回滚到上一个稳定版本
```
