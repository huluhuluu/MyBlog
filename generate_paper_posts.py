import os

def write_post(base_path, slug, title, content):
    path = os.path.join(base_path, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)

spec_dec_base = "content/post/speculative-decoding/blog"
on_device_base = "content/post/on-device-inference/blog"

# Speculative Decoding Papers
posts = [
    (spec_dec_base, "medusa-speculative", "MEDUSA: 多头解码与 Tree Attention", """---
title: "MEDUSA: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads"
date: 2026-04-02T10:10:00+08:00
slug: "medusa-speculative"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
Medusa 并不是一个独立的草稿模型，而是在主模型（Backbone）之上并行挂载了多个额外的解码头（Medusa Heads）。其核心组件包括：
1. **Medusa Heads**: 采用简单的 MLP 结构，每个头负责预测未来第 $k$ 个 token。
2. **Tree Attention**: 在验证阶段，Medusa 将所有头预测出的候选 token 组合成一个“树状”结构。大模型通过一次 Forward，利用特殊的 Attention Mask 并行处理这棵树上的所有路径。

## 深度分析
**优势**：
- **无需管理草稿模型**：省去了独立草稿模型的内存开销和模型间通信。
- **训练简单**：仅需冻结主模型，对 Medusa Heads 进行微调。
**对比分析**：
相比传统的 Speculative Decoding（如原始的 Leviathan 方案），Medusa 在推理时只需维持一个 KV Cache 状态。但其缺陷在于预测精度随长度增加迅速衰减，且由于是静态预测，缺乏自回归过程中的特征依赖，这正是后续 EAGLE 系列改进的切入点。
"""),
    (spec_dec_base, "eagle-speculative", "EAGLE: 特征级推测解码", """---
title: "EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty"
date: 2026-04-02T10:11:00+08:00
slug: "eagle-speculative"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
EAGLE 的核心洞察是：直接在词表层预测下一个 token 是不稳定的，应该在**特征层（Feature Level）**进行预测。
- **核心组件**：一个轻量级的 Transformer 层。
- **工作流程**：它将大模型的隐藏状态（Hidden States）作为输入，通过自回归的方式预测下一个隐藏状态。最后通过大模型的 LM Head 将预测出的特征转化为具体的 token。

## 深度分析
**优势**：
- **高接受率**：由于在特征层操作，捕获了更深层的语义信息，其接受率显著高于 Medusa。
- **输入信息量大**：融合了当前隐藏状态和上一个 token，减小了不确定性。
**对比分析**：
EAGLE 实际上是用一个小型的自回归模型来模拟大模型的行为。相比 Medusa 的静态 MLP，EAGLE 的“特征级自回归”更符合大模型的生成逻辑。虽然单步草稿生成开销略大，但极高的接受率（通常能达到 2-3x 的加速比）使其整体收益更高。
"""),
    (spec_dec_base, "eagle2-speculative", "EAGLE-2: 动态草稿树优化", """---
title: "EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees"
date: 2026-04-02T10:12:00+08:00
slug: "eagle2-speculative"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
EAGLE-2 在 EAGLE 的基础上引入了**动态草稿树（Dynamic Draft Trees）**。
- **机制**：在草稿生成过程中，它会根据当前步预测的置信度（Confidence Score）来动态决定下一步是继续深挖（增加深度）还是广撒网（增加宽度）。

## 深度分析
**分析**：
推测解码的一个痛点是“推测失败后的回退开销”。EAGLE-2 通过动态调整树的形状，确保了只有在大概率正确的情况下才进行长路径推测。相比 Medusa 固定的树结构，这种策略在处理逻辑复杂或歧义较多的文本时表现更稳健，有效避免了过度推测导致的算力浪费。
"""),
    (spec_dec_base, "eagle3-speculative", "EAGLE-3: 32k 词表剪枝与大规模扩展", """---
title: "EAGLE-3: Scaling up Inference Acceleration via Training-Time Test"
date: 2026-04-02T10:13:00+08:00
slug: "eagle3-speculative"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
EAGLE-3 代表了该系列的最新演进。其核心在于：
1. **训练时测试（Training-Time Test）**：将测试阶段的加速目标直接融入训练 Loss，使草稿模型更具鲁棒性。
2. **LM_Head 剪枝（32k 词表）**：针对常用的 Llama 系列模型，EAGLE-3 发现完整的 128k 词表对于草稿预测是冗余的。通过将其压缩并剪枝至 32k 左右，显著降低了 Softmax 和采样开销。

## 深度分析
**更高层次的分析**：
EAGLE-3 的成功标志着推测解码从“算法精修”走向了“系统级优化”。32k 词表的细节非常关键，因为在端侧或显存受限场景下，大词表的计算开销甚至能占到草稿生成的一半。EAGLE-3 通过剪枝将算力集中在核心语义预测上，配合其复杂的特征级回归，达到了目前开源方案中的加速比巅峰。
"""),
    (spec_dec_base, "dflash-speculative", "DFlash: 块状扩散推测解码", """---
title: "DFlash: Block Diffusion for Flash Speculative Decoding"
date: 2026-04-02T10:14:00+08:00
slug: "dflash-speculative"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
DFlash 另辟蹊径，引入了 **扩散模型（Diffusion）** 的思想来一次性生成一整块（Block）token。
- **思路**：与其一个个 token 往后猜，不如直接对一段固定长度的 token 序列进行非自回归的并行预测。

## 深度分析
**分析对比**：
DFlash 试图打破 EAGLE 的自回归限制。自回归草稿模型虽然准，但每生成一个 token 都要多一次串行依赖。DFlash 利用扩散过程并行生成，理论上极大缩短了草稿生成时间。但在准确性上，非自回归预测仍难以完全匹敌 EAGLE。该方法在追求极致 Throughput 的云侧大批量推理中极具潜力。
"""),
    (on_device_base, "asplos25-npu-llm", "ASPLOS 2025: NPU 深度加速", """---
title: "[ASPLOS 2025] Fast On-device LLM Inference with NPUs"
date: 2026-04-02T10:20:00+08:00
slug: "asplos25-npu-llm"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
这是近期端侧加速领域最重量级的论文之一。其核心贡献在于对移动端 NPU 底层指令集的深度榨取：
1. **指令级融合**：将内存密集型算子直接融合进计算单元指令流，减少数据搬运。
2. **混合精度量化**：针对 NPU 的 INT4/FP16 硬件特性，采用非对称量化策略。

## 深度分析
**更高层次的分析**：
长期以来，NPU 推理受限于私有协议和开发框架（如 SNPE）。这篇论文展示了通过深入硬件底层的算子定制，可以实现比通用 GPU 框架（如 MACE, MNN）快数倍的推理速度。它揭示了一个趋势：端侧 LLM 的终局必然是 NPU-First，因为 GPU 的功耗墙对于手机端 Agent 应用来说是无法逾越的。
"""),
    (on_device_base, "powerinfer2-smartphone", "PowerInfer-2: 稀疏激活优化", """---
title: "PowerInfer-2: Fast Large Language Model Inference on a Smartphone"
date: 2026-04-02T10:21:00+08:00
slug: "powerinfer2-smartphone"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
PowerInfer-2 是目前在智能手机上实现 10+ tokens/s 的代表性工作。
- **稀疏性（Sparcity）**：利用 LLM 神经元在推理时只有极小比例被激活的特性。
- **预测器机制**：通过一个极其轻量的预测器，在计算前判断哪些参数块（Neurons/Blocks）是活跃的。

## 深度分析
**对比分析**：
在移动 SoC 上，算力通常不是瓶颈，**内存带宽**才是。PowerInfer-2 的高明之处在于它不是试图跑得更快，而是试图“搬得更少”。通过稀疏激活只加载 10%-20% 的参数，直接绕过了内存带宽的物理限制。这是目前解决 7B+ 模型在主流手机上流畅运行最切实可行的方案。
"""),
    (on_device_base, "llm-in-flash-ssd", "LLM in a flash: 闪存交换推理", """---
title: "LLM in a flash: Efficient Large Language Model Inference with Limited Memory"
date: 2026-04-02T10:22:00+08:00
slug: "llm-in-flash-ssd"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
Apple 出品的经典论文，解决了“小内存手机跑大模型”的问题。
- **Windowing & Row-Column Bundling**: 将模型参数存储在闪存（NAND Flash）中，并采用滑动窗口加载机制，只保留当前活跃层的权重。
- **分析**：其核心在于最大化 SSD 的顺序读取性能，并与计算流水线重叠。

## 深度分析
**分析**：
该方案是对内存物理极限的挑战。它向我们展示了端侧 LLM 并不一定非要常驻 16GB 显存。通过牺牲一定的延迟（由于 SSD 与 RAM 的带宽差异），让 4GB 甚至 2GB 内存的旧设备也具备了运行 LLM 的入场券，极大地降低了端侧 AI 的硬件门槛。
""")
]

for base, slug, title, content in posts:
    write_post(base, slug, title, content)
