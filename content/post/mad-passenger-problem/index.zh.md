---
title: "疯子乘客问题：当博弈论遇上生死抉择"
date: 2026-02-26T00:35:00+08:00
lastmod: 2026-02-26T00:35:00+08:00
draft: false
description: "一个关于博弈论的经典思想实验"
slug: "mad-passenger-problem"
tags: ["博弈论", "悖论", "分享"]
categories: ["分享"]
comments: true
---

最近又看到一个有趣的博弈论问题，叫「疯子乘客问题」，和之前分享的蓝眼睛岛民悖论有点像，都是那种乍一看很简单，仔细一想又觉得哪里不对的题目。

## 1. 问题设定

故事是这样的：

你开着一辆车，车上坐着一个疯子。车行驶到一座桥上，桥下是深渊。疯子突然威胁你：

> **「如果你不把车开下去，我就引爆身上的炸弹，我们同归于尽。」**

问题是：**你相信他的威胁吗？你应该怎么做？**

<!-- 图片占位：场景示意图 -->
<!-- 文生图提示词：A car on a bridge over a deep canyon, dramatic sunset lighting, silhouette of two people inside the car, tension atmosphere, cinematic style illustration -->
![场景示意](images/bridge-scene.png)

## 2. 简单分析

看起来是个选择题：

| 选择 | 结果 |
|------|------|
| 相信他，开下去 | 你死了 |
| 不相信他，继续开 | 如果他真的引爆，你也死了 |

好像怎么选都是死路一条？

但仔细想想，疯子的威胁是可信的吗？

**如果疯子真的想同归于尽，他根本不需要威胁你，直接引爆就好了。** 他之所以威胁你，说明他可能更希望另一种结果——比如你把车开下去，他活下来。

所以这个威胁本身暴露了他的真实偏好：**他可能不想死**。

<!-- 图片占位：决策树示意图 -->
<!-- 文生图提示词：Decision tree diagram with branching paths, one branch leading to cliff, another to explosion, game theory visualization, clean infographic style -->
![决策树](images/decision-tree.png)

## 3. 威胁的可信性

这就涉及到博弈论中「**可信威胁**」的概念。

### 3.1 可信威胁的条件

一个威胁要可信，需要满足两个条件：

1. **威胁者有能力执行威胁**
2. **执行威胁对威胁者来说是最优选择**（或者至少不是最差选择）

<!-- 图片占位：可信威胁条件示意图 -->
<!-- 文生图提示词：Two-panel diagram showing "capability" and "incentive", icons representing bomb and decision, professional business presentation style -->
![可信威胁条件](images/credible-threat.png)

### 3.2 分析疯子的情况

在这个例子里：

- 疯子显然**有能力**引爆炸弹 ✓
- 但**执行威胁是不是他的最优选择**呢？ ✗

如果他的目的是「让你开车跳崖」，那当你拒绝时，他引爆炸弹——他自己也死了。这说明引爆炸弹**不是他的最优选择**，他可能只是在虚张声势。

## 4. 无穷递归

但问题来了：**如果疯子知道你会这样分析，他会怎么做？**

他可能会故意表现得「很疯狂」，让你相信他真的不在乎自己的性命。比如他可以：

- 眼神狂乱，口吐白沫
- 做一些非理性的行为
- 甚至先引爆一个小炸弹证明他是认真的

这就变成了一个「我相信你相信我相信……」的**无穷递归**。

<!-- 图片占位：递归思维示意图 -->
<!-- 文生图提示词：Infinite mirror reflection showing two figures, each mirror showing deeper level of strategic thinking, psychological thriller atmosphere, dark tones -->
![递归思维](images/infinite-recursion.png)

### 4.1 理性 vs 非理性

这就涉及到一个悖论：

- 如果疯子是**理性的**，他的威胁不可信（因为引爆对他也是死）
- 如果疯子是**非理性的**，他的威胁反而可信（因为他不在乎后果）
- 所以表现出「非理性」反而可能是**理性的选择**

## 5. 现实中的类比

这个问题让我想到国际关系中的「**核威慑**」。

一个国家宣称：「如果你攻击我，我就用核武器反击。」

这个威胁可信吗？如果对方真的攻击了，反击意味着双方都毁灭，那反击还是最优选择吗？

<!-- 图片占位：核威慑示意图 -->
<!-- 文生图提示词：World map with nuclear symbols, two opposing sides with missiles, Cold War era aesthetic, vintage propaganda poster style -->
![核威慑](images/nuclear-deterrence.png)

### 5.1 增加威胁可信性的策略

为了解决这个问题，国家会采取各种策略来增加威胁的可信性：

| 策略 | 说明 |
|------|------|
| 自动反击系统 | 死了也要报复，消除「反击不理性」的问题 |
| 公开承诺 | 让退出的代价高于执行威胁 |
| 培养不可预测形象 | 让对手无法理性分析 |

<!-- 图片占位：威慑策略示意图 -->
<!-- 文生图提示词：Three-panel infographic showing deterrence strategies, military defense system, political commitment, unpredictable behavior, clean modern design -->
![威慑策略](images/deterrence-strategies.png)

## 6. 小结

疯子乘客问题没有一个标准答案，但它揭示了博弈论中一个重要的概念：**威胁的可信性取决于双方的偏好和信息**。

**关键要点**：
- **可信威胁**：需要能力和激励两个条件
- **信号传递**：表现出非理性可能是理性的选择
- **无穷递归**：「我相信你相信我相信」的思维链条

有时候，看起来可怕的威胁可能只是虚张声势；而有时候，看似非理性的行为反而是理性的选择。

博弈论的有趣之处就在于此——它让我们思考：**「如果对方也像我一样在思考，他会怎么做？」**

---

如果你对这个问题感兴趣，可以搜索「madman theory」或者「credible threat」看看更多分析。