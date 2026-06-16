#!/bin/bash
# ==========================================================================
# Hermes Self-Evolution Kit - 一键启动脚本
# 用法: bash examples/quickstart.sh
# ==========================================================================

set -e

echo "========================================"
echo "  🧬 Hermes Self-Evolution Kit"
echo "  一键快速启动"
echo "========================================"

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 需要 Python 3.8+，请先安装"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
echo "✅ Python 版本: $PYTHON_VERSION"

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi
source venv/bin/activate

# 安装依赖
echo "📦 安装依赖..."
pip install -q -r requirements.txt 2>/dev/null || {
    echo "⚡ requirements.txt 不存在，使用 uv 快速安装..."
    pip install -q openai PyYAML sqlite-utils httpx pydantic rich
}

# 创建配置
if [ ! -f "config.yaml" ]; then
    echo "⚙️  从模板创建配置..."
    cp templates/evol_config.yaml config.yaml
    echo "⚠️  请编辑 config.yaml 填入你的 API Key"
    echo "   然后重新运行此脚本"
    exit 0
fi

# 检查 API Key
if grep -q "\${OPENAI_API_KEY}" config.yaml 2>/dev/null; then
    echo "⚠️  请先在 config.yaml 中配置 API Key"
    exit 1
fi

# 创建必要目录
mkdir -p data logs reports feedback

# 执行一次进化测试
echo ""
echo "🚀 执行单次进化测试..."
python -c "
from hermes_evol import EvolutionPipeline
p = EvolutionPipeline('config.yaml')
r = p.evolve('什么是强化学习？')
print(f'✅ 进化完成，评分: {r.top_score:.1f}')
"

echo ""
echo "========================================"
echo "  ✅ 启动完成!"
echo "  后续步骤:"
echo "  1. python scripts/install_cron.py  # 设置定时进化"
echo "  2. python scripts/view_report.py --latest  # 查看报告"
echo "========================================"
