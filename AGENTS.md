# Hugo Blog 项目说明

## 项目概述

这是 **huluhuluu** 的个人博客项目，基于 **Hugo** 静态网站生成器构建，使用 **hugo-theme-stack** 主题。博客已部署在 GitHub Pages：https://huluhuluu.github.io/

### 主要技术栈

- **Hugo Extended**: v0.155.3+ (需要 extended 版本以支持 SCSS/Sass)
- **hugo-theme-stack**: 卡片式博客主题 (GPL-3.0 许可证)
- **评论系统**: Giscus (基于 GitHub Discussions)
- **部署平台**: GitHub Pages + GitHub Actions

### 主题特性

- Giscus 评论系统支持
- PhotoSwipe 图片画廊
- Open Graph 元数据
- 深色/浅色模式切换
- 目录 (Table of Contents) - 带折叠功能
- 站内搜索
- 多语言支持 (当前配置为简体中文)
- 小组件系统 (搜索、归档、分类、标签云)
- Mermaid 图表支持
- 数学公式支持 (通过 Goldmark passthrough)
- Alert 容器 (note/tip/important/warning/caution)

---

## 目录结构

```
HugoBlog/
├── config/_default/       # 配置文件目录
│   ├── hugo.toml          # Hugo 核心配置
│   ├── params.toml        # 主题参数配置
│   ├── languages.toml     # 多语言和菜单配置
│   ├── markup.toml        # Markdown 渲染配置
│   └── related.toml       # 相关文章推荐配置
├── archetypes/            # 内容模板
│   └── default.md         # 新文章默认模板
├── assets/                # 自定义资源文件
│   ├── img/avatar.png     # 头像
│   └── scss/custom.scss   # 自定义样式
├── content/               # 博客内容
│   ├── _index.zh.md       # 首页配置
│   ├── page/              # 静态页面
│   │   ├── about/         # 关于页面
│   │   ├── archives/      # 归档页面
│   │   └── search/        # 搜索页面
│   └── post/              # 博客文章
│       ├── blue-eyed-islander-paradox/  # 蓝眼岛民悖论
│       ├── hugo-blog-setup/              # 博客搭建教程
│       ├── leetcode-logs/                # LeetCode 刷题记录 (Git 子模块)
│       ├── mad-passenger-problem/        # 疯狂乘客问题
│       ├── mnn-tutorial/                 # MNN 端侧部署教程 (Git 子模块)
│       ├── useful-tools/                 # 实用工具推荐 (Git 子模块)
│       └── zermelo-game-theory/          # 博弈论
├── layouts/               # 自定义布局模板
│   ├── _markup/render-image.html  # 图片渲染模板
│   └── _partials/
│       ├── article/components/     # 文章组件 (header, footer)
│       └── widget/toc.html         # 自定义 TOC 组件
├── static/                # 静态文件
│   └── img/avatar.png     # 头像 (静态副本)
├── themes/                # 主题目录 (Git 子模块)
│   └── hugo-theme-stack/
├── .github/workflows/     # GitHub Actions 工作流
│   └── update-submodules.yml  # 子模块更新工作流
└── public/                # 构建输出目录
```

---

## Git 子模块管理

项目使用多个 Git 子模块来管理独立的内容仓库：

| 子模块路径 | 仓库地址 | 说明 |
|-----------|---------|------|
| `themes/hugo-theme-stack` | CaiJimmy/hugo-theme-stack | 博客主题 |
| `content/post/mnn-tutorial` | huluhuluu/MNN-TUTORIAL | MNN 端侧部署教程 |
| `content/post/leetcode-logs` | huluhuluu/Leetcode-Logs | LeetCode 刷题记录 |
| `content/post/useful-tools` | huluhuluu/useful-tools | 实用工具推荐 |

### 子模块常用命令

```bash
# 初始化并拉取所有子模块
git submodule update --init --recursive

# 更新所有子模块到最新版本
git submodule update --remote --merge

# 更新单个子模块
git submodule update --remote themes/hugo-theme-stack
```

---

## 常用命令

### 本地开发

```bash
# 启动本地开发服务器 (默认 http://localhost:1313)
hugo server

# 启动开发服务器并包含草稿文章
hugo server -D

# 指定端口启动
hugo server -p 8080
```

### 内容创建

```bash
# 创建新文章
hugo new post/my-first-post/index.zh.md

# 创建新页面
hugo new page/about/index.zh.md
```

### 构建部署

```bash
# 构建静态网站 (输出到 public/ 目录)
hugo

# 构建并包含草稿
hugo -D

# 构建生产环境版本 (最小化)
hugo --minify
```

---

## 配置说明

### 核心配置 (hugo.toml)

```toml
baseURL                = "https://huluhuluu.github.io/"
languageCode           = "zh"
title                  = "huluhuluu"
defaultContentLanguage = "zh"
hasCJKLanguage         = true
theme                  = "hugo-theme-stack"

[pagination]
    pagerSize = 10

[permalinks]
    post = "/p/:slug/"
    page = "/:slug/"

# 模块挂载配置 (用于 MNN-TUTORIAL 子目录)
[module]
    [[module.mounts]]
        source = "content"
        target = "content"
        excludeFiles = ["post/mnn-tutorial/blog/**"]
    [[module.mounts]]
        source = "content/post/mnn-tutorial/blog"
        target = "content/post"
```

### 评论配置 (params.toml - Giscus)

```toml
[comments]
    enabled  = true
    provider = "giscus"

    [comments.giscus]
        repo             = "huluhuluu/MyBlog"
        category         = "Announcements"
        mapping          = "pathname"
        lightTheme       = "light"
        darkTheme        = "dark_dimmed"
        reactionsEnabled = 1
        lang             = "zh-CN"
```

### Markdown 渲染配置 (markup.toml)

```toml
[goldmark]
    [goldmark.extensions.passthrough]
        enable = true
        [goldmark.extensions.passthrough.delimiters]
            block  = [["\\[", "\\]"], ["$$", "$$"]]
            inline = [["\\(", "\\)"]]

[tableOfContents]
    endLevel   = 4
    startLevel = 1

[highlight]
    noClasses = false
    lineNos   = true
```

### 相关文章推荐配置 (related.toml)

```toml
includeNewer = true
threshold    = 60
toLower      = false
indices      = [
    { name = "tags", weight = 100 },
    { name = "categories", weight = 200 },
]
```

### 文章许可协议

```toml
[article.license]
    enabled = true
    default = "Licensed under CC BY-NC-SA 4.0"
```

---

## 内容编写规范

### 文章 Front Matter

```yaml
---
title: "文章标题"
date: 2024-01-01
lastmod: 2024-01-02
draft: false
description: "文章描述"
slug: "article-slug"
tags: ["标签1", "标签2"]
categories: ["分类"]
comments: true
---
```

### 文章目录结构

建议每篇文章使用独立目录，方便管理图片资源：

```
content/post/my-article/
├── index.zh.md      # 文章内容
└── images/          # 文章图片
    ├── image1.png
    └── image2.png
```

### Markdown 扩展功能

- **数学公式**: 使用 `$...$` (行内) 或 `$$...$$` (块级)
- **代码高亮**: 支持语法高亮和行号
- **Mermaid 图表**: 使用 ```mermaid 代码块
- **Alert 容器**: 支持 note/tip/important/warning/caution

---

## 自定义组件

### TOC 目录组件

项目实现了自定义的 TOC 组件 (`layouts/_partials/widget/toc.html`)，功能包括：

- 三级目录折叠功能
- 一键折叠/展开按钮 (仅控制三级目录)
- 二级目录独立折叠按钮
- 滚动条样式优化
- 深色模式适配

### 自定义样式

在 `assets/scss/custom.scss` 中定义了：

- 侧边栏间距调整
- TOC 目录样式 (圆角卡片、折叠按钮)
- 分页组件居中
- 滚动条美化
- 深色模式适配

---

## 部署说明

### 当前部署方案

博客使用 **GitHub Pages** 部署，通过 **GitHub Actions** 自动构建。

### 子模块更新工作流

`.github/workflows/update-submodules.yml` 用于自动更新主题子模块：

- 触发方式：`repository_dispatch` 或手动触发
- 功能：自动拉取主题最新代码并提交
- 需要 `PAT` (Personal Access Token) 作为 Secret

---

## 特殊功能

### 多内容源挂载

项目配置了 Hugo 模块挂载，将 `content/post/mnn-tutorial/blog` 目录的内容作为独立文章挂载：

```toml
[module]
    [[module.mounts]]
        source = "content/post/mnn-tutorial/blog"
        target = "content/post"
```

这允许 MNN 教程系列文章在独立子目录中管理，同时作为博客文章发布。

**注意**: `leetcode-logs` 和 `useful-tools` 子模块通过各自目录下的 `index.zh.md` 文件引用子模块内容，未使用模块挂载。

---

## 开发约定

### 自定义覆盖

1. **覆盖主题模板**: 在 `layouts/` 目录中创建同名模板文件
2. **覆盖主题样式**: 在 `assets/scss/custom.scss` 中添加自定义样式
3. **覆盖主题翻译**: 在 `i18n/` 目录中创建同名翻译文件

### 资源管理

- 图片资源放在文章目录的 `images/` 子目录或 `assets/` 目录
- `assets/` 中的资源会被 Hugo 处理 (压缩、指纹等)
- `static/` 中的资源直接复制到输出目录

---

## 博客文章索引

| 文章 | 分类 | 说明 |
|------|------|------|
| [个人博客搭建记录](/p/hugo-blog-setup/) | 技术记录 | Hugo + GitHub + Vercel 搭建教程 |
| [MNN端侧部署教程](/p/mnn-tutorial/) | MNN端侧部署 | MNN 框架从环境配置到 LLM 部署 |
| [LeetCode 刷题记录](/p/leetcode-logs/) | LeetCode | 每日刷题、Hot100、总结 |
| [实用工具推荐](/p/useful-tools/) | 工具 | VSCode、AI Agent、终端工具配置 |
| [蓝眼岛民悖论](/p/blue-eyed-islander-paradox/) | - | 逻辑推理 |
| [疯狂乘客问题](/p/mad-passenger-problem/) | - | 概率问题 |
| [博弈论](/p/zermelo-game-theory/) | - | Zermelo 博弈论 |

---

## 参考资源

- [Hugo 官方文档](https://gohugo.io/documentation/)
- [Stack 主题文档](https://stack.cai.im)
- [Stack 主题中文文档](https://stack.cai.im/zh)
- [Stack 主题 GitHub](https://github.com/CaiJimmy/hugo-theme-stack)
- [Giscus 评论系统](https://giscus.app/zh-CN)
