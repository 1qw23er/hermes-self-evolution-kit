#!/usr/bin/env python3
"""
Hermes Self-Evolution Kit - 基础使用示例

这个示例展示了如何使用 EvolutionPipeline 进行单次和批量进化。
"""

import json
import sys
from pathlib import Path

# 将项目根目录加入路径
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from hermes_evol import EvolutionPipeline
except ImportError:
    print("❌ 请先安装 hermes-self-evolution-kit")
    print("   pip install -e .")
    sys.exit(1)


def basic_usage():
    """基础用法：单次进化"""
    print("=" * 60)
    print("🚀 Hermes Self-Evolution Kit - 基础示例")
    print("=" * 60)

    # 初始化进化管道
    pipeline = EvolutionPipeline(config="config.yaml")

    # 要进化的问题
    prompt = "请用通俗的语言解释什么是深度学习？"

    print(f"\n📝 进化问题: {prompt}")
    print("⏳ 正在进化...")

    # 执行单次进化
    result = pipeline.evolve(prompt)

    print(f"\n✅ 进化完成!")
    print(f"📊 最佳评分: {result.top_score:.1f}")
    print(f"📋 评分详情: {json.dumps(result.scores, indent=2, ensure_ascii=False)}")
    print(f"💡 最佳回答 (前100字): {result.best_answer[:100]}...")

    return result


def batch_evolution():
    """批量进化示例"""
    print("\n" + "=" * 60)
    print("📦 批量进化")
    print("=" * 60)

    pipeline = EvolutionPipeline(config="config.yaml")

    prompts = [
        "什么是反向传播算法？",
        "解释注意力机制的原理",
        "Python 中 GIL 是什么？有哪些规避方法？",
    ]

    results = pipeline.evolve_batch(prompts)

    for i, (prompt, result) in enumerate(zip(prompts, results)):
        print(f"\n[{i+1}] 📝 {prompt[:40]}...")
        print(f"    📊 评分: {result.top_score:.1f}")

    return results


def view_history():
    """查看进化历史"""
    print("\n" + "=" * 60)
    print("📜 进化历史")
    print("=" * 60)

    pipeline = EvolutionPipeline(config="config.yaml")
    history = pipeline.get_history(limit=5)

    for entry in history:
        print(f"  🆔 Round {entry.round:>3} | "
              f"📊 {entry.score:5.1f} | "
              f"📅 {entry.timestamp}")

    return history


if __name__ == "__main__":
    # 执行所有示例
    basic_usage()
    batch_evolution()
    view_history()
