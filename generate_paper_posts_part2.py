import os

def write_post(base_path, slug, title, content):
    path = os.path.join(base_path, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.md"), "w", encoding="utf-8") as f:
        f.write(content)

spec_dec_base = "content/post/speculative-decoding/blog"
on_device_base = "content/post/on-device-inference/blog"

posts = [
    (spec_dec_base, "p-eagle-speculative", "P-EAGLE: 并行草稿生成与可扩展训练", """---
title: "P-EAGLE: Parallel-Drafting EAGLE with Scalable Training"
date: 2026-04-02T10:15:00+08:00
slug: "p-eagle-speculative"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
P-EAGLE 旨在解决 EAGLE 训练慢、生成仍有部分串行依赖的问题。
- **并行化 (Parallelism)**：通过优化数据流，支持多级草稿头的同时预测。
- **可扩展性 (Scalable Training)**：引入了更适合分布式训练的架构设计。

## 深度分析
**更高层次的分析**：
EAGLE 系列最核心的痛点在于它实际上引入了一个额外的、不可忽视的小模型。P-EAGLE 的改进在于其工业化的落地，通过并行草稿预测，降低了生成时延。相比 Medusa 的简单并行，P-EAGLE 保持了特征层的高精度，同时在吞吐量（Throughput）上补齐了短板。
"""),
    (spec_dec_base, "spec-spec-decoding", "Speculative Speculative Decoding: 双重推测解码", """---
title: "Speculative Speculative Decoding"
date: 2026-04-02T10:16:00+08:00
slug: "spec-spec-decoding"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
这是一个非常套娃（Recursive）的思路：推测中再套一层推测。
- **结构**：大模型（L）验证草稿模型（D1），而草稿模型（D1）又由更小的草稿模型（D2）来推测。

## 深度分析
**分析**：
虽然听起来复杂，但其背后的逻辑很清晰：草稿模型本身如果是 1B 或 2B 大小，在 GPU 上生成仍然有开销。如果用一个 100M 的极小模型来加速 1B 模型，再用 1B 模型加速 70B 模型，可以进一步压榨推理链路。但其实际收益受限于层层推测的误差累积（Cascading Error），对训练质量的要求极高。
"""),
    (spec_dec_base, "spec-vocabulary-pruning", "Speculative Vocabulary: 基于剪枝词表的优化", """---
title: "Speculative Decoding with a Speculative Vocabulary"
date: 2026-04-02T10:17:00+08:00
slug: "spec-vocabulary-pruning"
tags: ["speculative-decoding"]
categories: ["paper"]
---
## 核心结构与内容
该论文专注于降低推测解码中的“Softmax 带宽”。
- **方法**：通过分析大模型的高频 token 分布，剪枝掉草稿模型中 80% 的罕见词汇。

## 深度分析
**细节分析**：
这在端侧极其有效。由于 Llama3 采用了 128k 的大词表，草稿模型即使参数量小，最后一步的分类头（Embedding & Linear）开销也极大。通过裁剪到 32k 甚至更小，不仅节省了显存，还极大缩短了草稿生成时间。
"""),
    (on_device_base, "dynamic-sparse-attention", "Dynamic Sparse Attention on Mobile SoCs", """---
title: "Dynamic Sparse Attention on Mobile SoCs"
date: 2026-04-02T10:30:00+08:00
slug: "dynamic-sparse-attention"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
针对手机 SoC 的算力特性，提出动态稀疏注意力机制。
- **核心逻辑**：在 Attention 计算中，动态丢弃掉关联度极低的部分，减少 KV Cache 读写。

## 深度分析
**更高层次的分析**：
Attention 机制在长文本下的 $O(n^2)$ 复杂度是手机散热和能耗的最大敌人。动态稀疏化不仅减少了计算量，更关键的是它降低了数据搬运的总能量消耗，是端侧长文对话（Agent 场景）的必备技术。
"""),
    (on_device_base, "agent-xpu-scheduling", "Agent.xpu: 异构 SoC 上的任务调度", """---
title: "Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC"
date: 2026-04-02T10:31:00+08:00
slug: "agent-xpu-scheduling"
tags: ["on-device"]
categories: ["paper"]
---
## 核心结构与内容
随着 Agentic 工作流（如搜索、工具调用）的普及，单一的推理加速已经不够了。
- **异构调度**：根据任务类型（是密集推理、还是逻辑判断、还是工具调用），在 CPU、GPU 和 NPU 之间实时切换负载。

## 深度分析
**分析**：
未来的端侧 AI 将是一个多模型、多任务的协作体。Agent.xpu 的前瞻性在于它从单纯的“模型加速”跃迁到了“全链路资源调度”。这对手机端的长续航和多任务并发至关重要。
""")
]

for base, slug, title, content in posts:
    write_post(base, slug, title, content)
