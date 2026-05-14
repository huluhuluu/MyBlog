# Draft Content TODO

> 更新时间：`2026-05-14`
>
> 统计范围：`content/post/*` 子仓库中所有带 `draft: true` 的 Markdown 内容，已排除主题模板。

## 维护约定

- 未完成内容保留为 `- [ ]`
- 发布前：文章内仍保持 `draft: true`
- 发布时：将文章改为 `draft: false`，同步 `lastmod`，并从本文件移除或勾选归档

## 草稿总览

| 子仓库 | 草稿数 | 说明 |
| --- | ---: | --- |
| `paper-view` | 13 | 论文解读与综述，当前草稿最多 |
| `simd-tutorial` | 5 | 系列首页 1 篇，子文章 4 篇 |
| `mnn-tutorial` | 5 | README 总览 1 篇，子文章 4 篇 |
| `opencl-tutorial` | 2 | OpenCL / MNN OpenCL 两篇 |
| `transformers-code-view` | 5 | 系列首页 1 篇，子文章 4 篇 |
| `useful-tools` | 1 | 仅剩 Ubuntu 代理配置草稿 |
| `leetcode-logs` | 1 | README 总览草稿 |
| **合计** | **32** | **7 个子仓库存在草稿** |

当前无 `draft: true` 内容的子仓库：`brain-candy`、`qnn-tutorial`

## 分仓库清单

### `simd-tutorial` · 5

路径：`content/post/simd-tutorial`

| 状态 | 类型 | 标题 | 最后更新 | Slug |
| --- | --- | --- | --- | --- |
| [ ] | index | [ARM SIMD 教程](./content/post/simd-tutorial/index.md) | `2026-04-15` | `arm-simd-tutorial` |
| [ ] | article | [ARM SIMD / NEON 基础](./content/post/simd-tutorial/blog/arm-simd-intro/index.md) | `2026-04-15` | `arm-simd-intro` |
| [ ] | article | [NEON 内在函数与数据搬运](./content/post/simd-tutorial/blog/neon-intrinsics/index.md) | `2026-04-15` | `neon-intrinsics` |
| [ ] | article | [NEON GEMM 微内核思路](./content/post/simd-tutorial/blog/neon-gemm/index.md) | `2026-04-15` | `neon-gemm` |
| [ ] | article | [Android 端基准与调优](./content/post/simd-tutorial/blog/arm-simd-benchmark/index.md) | `2026-04-15` | `arm-simd-benchmark` |

### `leetcode-logs` · 1

路径：`content/post/leetcode-logs`

| 状态 | 类型 | 标题 | 最后更新 | Slug |
| --- | --- | --- | --- | --- |
| [ ] | README | [Leetcode-Logs](./content/post/leetcode-logs/README.md) | `-` | `-` |

### `mnn-tutorial` · 5

路径：`content/post/mnn-tutorial`

| 状态 | 类型 | 标题 | 最后更新 | Slug |
| --- | --- | --- | --- | --- |
| [ ] | README | [mnntutorial](./content/post/mnn-tutorial/README.md) | `2026-02-26` | `mnn-tutorial` |
| [ ] | article | [MNN 工厂模式介绍](./content/post/mnn-tutorial/blog/introduce-factory/index.md) | `2026-02-26` | `introduce-factory` |
| [ ] | article | [MNN-LLM 配置](./content/post/mnn-tutorial/blog/llm-config/index.md) | `2026-02-26` | `llm-config` |
| [ ] | article | [MNN-LLM 加载流程](./content/post/mnn-tutorial/blog/llm-load/index.md) | `2026-02-26` | `llm-load` |
| [ ] | article | [MNN-LLM 推理流程](./content/post/mnn-tutorial/blog/llm-infer/index.md) | `2026-02-26` | `llm-infer` |

### `opencl-tutorial` · 2

路径：`content/post/opencl-tutorial`

| 状态 | 类型 | 标题 | 最后更新 | Slug |
| --- | --- | --- | --- | --- |
| [ ] | article | [Qualcomm OpenCL](./content/post/opencl-tutorial/blog/opencl-qualcomm/index.md) | `2026-04-20` | `opencl-qualcomm` |
| [ ] | article | [MNN OpenCL `matmul_buf.cl` 解析](./content/post/opencl-tutorial/blog/mnn-opencl-matmul-buf/index.md) | `2026-04-19` | `mnn-opencl-matmul-buf` |

### `paper-view` · 13

路径：`content/post/paper-view`

| 状态 | 类型 | 标题 | 最后更新 | Slug |
| --- | --- | --- | --- | --- |
| [ ] | article | [端侧 LLM 推理优化 系列论文深度解析](./content/post/paper-view/blog/on-device-inference/index.md) | `2026-04-15` | `on-device-inference-overview` |
| [ ] | article | [PowerInfer-2: Fast Large Language Model Inference on a Smartphone](./content/post/paper-view/blog/on-device-inference/powerinfer2-smartphone/index.md) | `2026-04-15` | `powerinfer2-smartphone` |
| [ ] | article | [LLM in a Flash: Efficient Large Language Model Inference with Limited Memory](./content/post/paper-view/blog/on-device-inference/llm-in-flash-ssd/index.md) | `2026-04-15` | `llm-in-flash-ssd` |
| [ ] | article | [Dynamic Sparse Attention on Mobile SoCs](./content/post/paper-view/blog/on-device-inference/dynamic-sparse-attention/index.md) | `2026-04-15` | `dynamic-sparse-attention` |
| [ ] | article | [Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC](./content/post/paper-view/blog/on-device-inference/agent-xpu-scheduling/index.md) | `2026-04-15` | `agent-xpu-scheduling` |
| [ ] | article | [HeteroLLM: Accelerating Large Language Model Inference on Mobile SoCs with Heterogeneous AI Accelerators](./content/post/paper-view/blog/on-device-inference/heterollm-soc/index.md) | `2026-04-15` | `heterollm-soc` |
| [ ] | article | [LLM Inference at the Edge: Mobile, NPU, and GPU Benchmarks](./content/post/paper-view/blog/on-device-inference/llm-inference-edge/index.md) | `2026-04-15` | `llm-inference-edge` |
| [ ] | article | [Scaling Test-time Compute for LLM Agents](./content/post/paper-view/blog/on-device-inference/scaling-test-time/index.md) | `2026-04-15` | `scaling-test-time` |
| [ ] | article | [推测解码 系列论文深度解析](./content/post/paper-view/blog/speculative-decoding/index.md) | `2026-04-02` | `speculative-decoding-overview` |
| [ ] | article | [LLM 量化技术深度解析](./content/post/paper-view/blog/quantization/index.md) | `2026-04-15` | `llm-quantization` |
| [ ] | article | [LoRA 高效微调技术深度解析](./content/post/paper-view/blog/lora-finetuning/index.md) | `2026-04-15` | `lora-finetuning` |
| [ ] | article | [LLM Test-Time Compute Scaling 深度解析](./content/post/paper-view/blog/test-time-scaling/index.md) | `2026-04-15` | `test-time-scaling` |
| [ ] | article | [LLM 推理系统优化深度解析](./content/post/paper-view/blog/llm-inference-optimization/index.md) | `2026-04-15` | `llm-inference-optimization` |

### `transformers-code-view` · 5

路径：`content/post/transformers-code-view`

| 状态 | 类型 | 标题 | 最后更新 | Slug |
| --- | --- | --- | --- | --- |
| [ ] | index | [Transformers 源码解析](./content/post/transformers-code-view/index.md) | `2026-05-14` | `transformers-code-view` |
| [ ] | article | [Qwen3 代码阅读: Module Construction](./content/post/transformers-code-view/blog/module-construction/index.md) | `2026-04-03` | `transformers-module-construction` |
| [ ] | article | [Qwen3 代码阅读: Attention 机制](./content/post/transformers-code-view/blog/attention-mechanisms/index.md) | `2026-04-03` | `transformers-attention` |
| [ ] | article | [Qwen3 代码阅读: KV Cache](./content/post/transformers-code-view/blog/kv-cache/index.md) | `2026-04-03` | `transformers-kv-cache` |
| [ ] | article | [Qwen3 代码阅读: Fine Tune and Loss](./content/post/transformers-code-view/blog/finetune-and-loss/index.md) | `2026-04-03` | `transformers-finetune-loss` |

### `useful-tools` · 1

路径：`content/post/useful-tools`

| 状态 | 类型 | 标题 | 最后更新 | Slug |
| --- | --- | --- | --- | --- |
| [ ] | article | [Ubuntu 代理配置](./content/post/useful-tools/blog/ubuntu-proxy/index.md) | `2026-01-30` | `ubuntu-proxy` |
