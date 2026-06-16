# 📦 安装指南

## 系统要求

| 项目 | 最低要求 | 推荐 |
|------|---------|------|
| Python | 3.8 | 3.11+ |
| 内存 | 2 GB | 8 GB |
| 磁盘 | 100 MB | 1 GB (含进化数据) |
| 网络 | 可访问 LLM API 端点 | 低延迟连接 |

## 安装方式

### 方式一：pip 安装（推荐）

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 安装包
pip install hermes-self-evolution-kit
```

### 方式二：源码安装

```bash
git clone https://github.com/your-org/hermes-self-evolution-kit.git
cd hermes-self-evolution-kit
pip install -e .
```

### 方式三：Docker（敬请期待）

```bash
docker pull nousresearch/hermes-self-evolution-kit
docker run -d --name hermes-evol nousresearch/hermes-self-evolution-kit
```

## 依赖列表

```text
# requirements.txt
openai>=1.0.0
PyYAML>=6.0
sqlite-utils>=3.0
httpx>=0.25.0
pydantic>=2.0.0
rich>=13.0.0
```

## 验证安装

```bash
python -c "from hermes_evol import EvolutionPipeline; print('✅ 安装成功')"
```
