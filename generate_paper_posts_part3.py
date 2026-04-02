import os

def write_post(base_path, slug, title, content):
    path = os.path.join(base_path, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)

on_device_base = "content/post/on-device-inference/blog"

posts = [
    (on_device_base, "heterollm-soc", "HeteroLLM: 异构芯片加速推断", """---
title: "HeteroLLM: Accelerating Large Language Model Inference on Mobile SoCs"
date: 2026-04-02T10:32:00+08:00
slug: "heterollm-soc"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
通过在多个异构加速器（GPU, NPU, DSP）上分块并行执行不同的 LLM 层或算子。
- **动态流水线**：实时监测不同核心的功耗和负载，动态负载均衡。

## 深度分析
**分析**：
HeteroLLM 填补了不同 AI 加速器间的算力鸿沟。手机端其实有很多“空闲”算力散落在 DSP 中，将其集成进 LLM 推理全流程，不仅能提速，更能分担 GPU 的发热压力。相比单纯使用单一处理器，异构协作在端侧能实现更高的能效比（Perf/Watt）。
"""),
    (on_device_base, "llm-inference-edge", "LLM Inference at the Edge: 移动 NPU 与 GPU 对比", """---
title: "LLM Inference at the Edge: Mobile, NPU, and GPU"
date: 2026-04-02T10:33:00+08:00
slug: "llm-inference-edge"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
这篇论文是对移动端推理平台（手机、嵌入式）的一次深度 Benchmark。
- **结论**：在批处理量为 1 时（常见端侧场景），NPU 的单位功耗性能通常优于 GPU 20% 以上。

## 深度分析
**分析对比**：
目前端侧 AI 的现状是“GPU 容易开发，NPU 上限更高”。由于 NPU 是专为矩阵乘法设计的固定电路，其静态功耗低、带宽利用率高。该论文为端侧开发者指明了方向：虽然 NPU 生态目前较碎，但对于需要全天候工作的手机 AI 助手，转向 NPU 是唯一的出路。
"""),
    (on_device_base, "scaling-test-time", "Scaling Test-time Compute for LLM Agents", """---
title: "Scaling Test-time Compute for LLM Agents"
date: 2026-04-02T10:34:00+08:00
slug: "scaling-test-time"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
探讨在端侧如何通过“增加思考时间（Test-time Compute）”让小模型达到大模型的效果。
- **方法**：在 Agent 推理阶段引入 Self-Consistency（自一致性）和 Beam Search。

## 深度分析
**分析**：
端侧跑不动 70B，但如果让 7B 多跑几遍、或者生成几个候选再评估，性能（推理准确性）可能接近甚至超过单次 Forward 的 70B。这种“以时间换质量”的策略在端侧异步推理场景（如离线总结）中极具吸引力。
"""),
    (on_device_base, "scaling-on-device-gpu", "Scaling On-Device GPU Inference for Large Generative Models", """---
title: "Scaling On-Device GPU Inference for Large Generative Models"
date: 2026-04-02T10:35:00+08:00
slug: "scaling-on-device-gpu"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
分析大规模生成模型在移动 GPU 上的扩展性限制。
- **核心结论**：随着 Context 增加，端侧 GPU 的算力释放受到显存读写速度的严格压制（Bandwidth Bound）。

## 深度分析
**分析对比**：
该论文警告我们：仅仅通过算子融合（Operator Fusion）只能解决局部问题。在端侧真正要实现长文本处理，必须从全局内存布局出发。这也印证了为什么 PowerInfer-2 的稀疏激活在目前是最顶级的方案——因为它直接削减了带宽需求。
""")
]

for base, slug, title, content in posts:
    write_post(base, slug, title, content)
