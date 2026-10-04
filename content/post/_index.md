---
title: "全部文章"
description: "论文研读、blog搭建、实用工具等所有博客内容。"
url: "/p/"
hide_list: true
---

# 全部文章

欢迎来到我的博客！这里汇集了我在技术学习过程中的笔记和心得。

---

## 📚 论文研读

### 推测解码 (Speculative Decoding)
- [推测解码系列论文深度解析](/p/speculative-decoding-overview/) - MEDUSA、EAGLE 系列、DFlash 等论文解析

### 端侧推理优化 (On-device Inference)
- [Fast On-device LLM Inference with NPUs](paper-view/blog/on-device-inference/asplos25-npu-llm/index.md) - NPU 指令级融合，20+ tokens/s
- [shadowAttn: Dynamic Sparse Attention](/p/dynamic-sparse-attention/) - NPU-centric 稀疏注意力
- [Agent.xpu](/p/agent-xpu-scheduling/) - Agentic LLM 流调度
- [HeteroLLM](/p/heterollm-soc/) - 层级/张量级异构执行
- [LLM in a Flash](/p/llm-in-flash-ssd/) - 闪存为缓存，突破内存限制
- [LLM Inference at the Edge](/p/llm-inference-edge/) - NPU vs GPU Benchmark
- [Scaling Test-time Compute](/p/scaling-test-time/) - Test-time 扩展
- [PowerInfer-2](/p/powerinfer2-smartphone/) - 稀疏性利用，动态权重加载

### LLM 量化技术 (Quantization)
- [LLM 量化技术深度解析](/p/llm-quantization/) - LLM.int8()、SmoothQuant、AWQ 论文解析

### 高效微调技术 (LoRA Fine-tuning)
- [LoRA 高效微调技术深度解析](/p/lora-finetuning/) - LoRA、QLoRA、PISSA、LoRA-GA 论文解析

### Test-Time Compute Scaling
- [LLM Test-Time Compute Scaling 深度解析](/p/test-time-scaling/) - 推理时计算扩展策略

### LLM 推理系统优化
- [LLM 推理系统优化深度解析](/p/llm-inference-optimization/) - FlashAttention、PagedAttention、Continuous Batching

---

## 🛠 实用工具

### 工具推荐合集
- [实用工具推荐](useful-tools/index.md) - VSCode、AI Agent、终端工具配置等

### AI 编程助手
- [Claude Code 使用指南](useful-tools/blog/claude-code/index.md) - Anthropic 官方编程助手
- [GitHub Copilot 配置](useful-tools/blog/copilot/index.md) - 代码补全配置
- [Codex CLI 配置](useful-tools/blog/codex-cli-config/index.md) - OpenAI 命令行工具
- [iFlow CLI 使用](useful-tools/blog/iflow/index.md) - 心流 CLI 工具

---

## 💻 编程学习

### LeetCode 刷题
- [LeetCode 刷题记录](leetcode-logs/index.md) - 每日一题、Hot100、总结
- [LeetCode 每日一题](leetcode-logs/blog/daily/index.md) - 按日期整理
- [LeetCode Hot100](leetcode-logs/blog/hot100/index.md) - 热门题目解析
- [LeetCode 总结](leetcode-logs/blog/summary/index.md) - 算法模板和技巧

### Transformers 源码解析
- [Transformers 源码阅读](/p/transformers-code-view/) - HuggingFace Transformers 深度解析

### 语言与文件格式
- [语言与文件格式备忘](language-file-cheatsheets/blog/_index.md) - 8 种语言核心语法 + 5 种文件格式速查

---

## 📱 端侧部署

### MNN 教程
- [MNN 端侧部署教程](/p/mnn-tutorial/) - 从环境配置到 LLM 部署

### QNN 教程
- [QNN 入门介绍](qnn-tutorial/blog/qnn-intro/index.md) - Qualcomm AI 引擎概述
- [QNN 环境搭建](/p/qnn-setup/) - 开发环境配置
- [QNN 量化指南](/p/qnn-quantization/) - 模型量化实践
- [QNN 教程合集](qnn-tutorial/index.md) - 完整教程系列

### OpenCL 教程
- [OpenCL 入门](opencl-tutorial/blog/opencl-intro/index.md) - 并行计算基础
- [OpenCL 环境搭建](/p/opencl-setup/) - 开发环境配置
- [Hello OpenCL](opencl-tutorial/blog/hello-opencl/index.md) - 第一个程序
- [OpenCL 教程合集](opencl-tutorial/index.md) - 完整教程系列

---

## 🔧 系统配置

### Linux 环境
- [Ubuntu 配置指南](useful-tools/blog/ubuntu-config/index.md) - 系统初始化
- [Git 常用命令](useful-tools/blog/git-commands/index.md) - 版本控制
- [Linux 常用命令](useful-tools/blog/linux-commands/index.md) - 命令速查
- [Docker 常用命令](useful-tools/blog/docker-commands/index.md) - 容器操作

### 终端工具
- [Zsh 配置](useful-tools/blog/zsh/index.md) - Shell 美化
- [Tmux 使用指南](useful-tools/blog/tmux/index.md) - 终端复用
- [fzf 模糊搜索](useful-tools/blog/fzf/index.md) - 快速查找
- [Zoxide 目录跳转](useful-tools/blog/zoxide/index.md) - 智能 cd
- [PWSH7 迁移](useful-tools/blog/pwsh7-migration/index.md) - PowerShell 7

### Vim/编辑器
- [Vim 常用命令](useful-tools/blog/vim-commands/index.md) - 编辑器操作
- [Flash VSCode](useful-tools/blog/flash-vscode/index.md) - 快速上手

---

## 🌐 网络与调试

### 网络工具
- [SSH 使用指南](useful-tools/blog/ssh-guide/index.md) - 远程连接
- [Netcat 网络工具](useful-tools/blog/netcat/index.md) - 网络调试
- [Wireshark 使用](useful-tools/blog/wireshark-guide/index.md) - 抓包分析

### Android 开发
- [ADB 使用指南](useful-tools/blog/adb-guide/index.md) - Android 调试桥
- [Remote ADB](mnn-tutorial/blog/remote-adb/index.md) - 远程调试
- [Termux 配置](useful-tools/blog/termux-config/index.md) - 手机终端

### Jetson 开发
- [Jetson 配置指南](useful-tools/blog/jetson-config/index.md) - NVIDIA 开发板

---

## 📦 开发环境

### Python 环境
- [Python 环境管理](useful-tools/blog/python-env/index.md) - conda/venv

### 包管理器
- [包管理器概览](useful-tools/blog/package-managers/index.md) - pip/apt/brew 等

### 交叉编译
- [交叉编译指南](mnn-tutorial/blog/cross-compiler/index.md) - 跨平台编译

---

## 🧠 思维训练

### 趣味数学
- [蓝眼岛民悖论](brain-candy/blog/blue-eyed-islander-paradox/index.md) - 逻辑推理
- [疯狂乘客问题](brain-candy/blog/airplane-seat-probability/index.md) - 概率问题
- [Zermelo 博弈论](brain-candy/blog/zermelo-game-theory/index.md) - 博弈论基础

### 思维糖果
- [Brain Candy](brain-candy/index.md) - 趣味博客、逻辑、辩论等思维糖果

---

## 📝 其他

### 博客搭建
- [个人博客搭建记录](hugo-blog-setup/index.md) - Hugo + GitHub Pages

### 模型下载
- [模型下载工具](useful-tools/blog/model-downloader/index.md) - HuggingFace 模型加速

---

## 📂 分类导航

- [LeetCode 刷题](/categories/leetcode/)
- [MNN 端侧部署](/categories/mnn/)
- [OpenCL 教程](/categories/opencl/)
- [论文阅读](/categories/paper/)
- [QNN 教程](/categories/qnn/)
- [分享](/categories/sharing/)
- [源码阅读](/categories/source_code/)
- [技术记录](/categories/technical/)
- [工具](/categories/tools/)
