# huluhuluu 的个人博客

基于 [Hugo](https://gohugo.io/) + [hugo-theme-stack](https://github.com/CaiJimmy/hugo-theme-stack) +  [Vercel](https://vercel.com/) 构建的个人博客。

## 站点信息

- **站点地址**: https://my-blog-p39q.vercel.app/
- **主题**: [hugo-theme-stack](https://github.com/CaiJimmy/hugo-theme-stack)
- **评论系统**: [Giscus](https://github.com/giscus/giscus)

## 目录结构

```
.
├── archetypes/          # 文章模板
├── assets/              # 静态资源 (SCSS, JS, 图片)
│   ├── img/             # 头像等图片
│   └── scss/            # 自定义样式
├── config/              # Hugo 配置
│   └── _default/        # 默认配置文件
├── content/             # 博客内容
│   ├── page/            # 独立页面 (关于、归档、搜索)
│   └── post/            # 博客文章
├── layouts/             # 自定义布局模板
├── static/              # 静态文件
├── themes/              # 主题 (git submodule)
│   └── hugo-theme-stack/
└── public/              # 构建输出 (git ignored)
```

## 子模块

本博客使用 git submodules 管理部分内容：

| 子模块 | 说明 |
|--------|------|
| `themes/hugo-theme-stack` | 博客主题 |
| `content/post/useful-tools` | 实用工具与配置速查 |
| `content/post/mnn-tutorial` | MNN 端侧部署教程 |
| `content/post/leetcode-logs` | LeetCode 刷题记录 |
| `content/post/qnn-tutorial` | 高通 QNN 教程 |
| `content/post/opencl-tutorial` | OpenCL 教程 |
| `content/post/paper-view` | 论文研读 |
| `content/post/transformers-code-view` | Transformers 源码解析 |
| `content/post/brain-candy` | 趣味思维题 |
| `content/post/simd-tutorial` | SIMD 教程 |
| `content/post/language-file-cheatsheets` | 语言与文件格式速查 |

## 链接约定

正文里的跳转链接要在 **GitHub 和渲染站点两端都能点**，写法取决于目标位置：

### 同仓库内跳转 → 相对路径

`content/post/<模块>/` 各自是独立仓库，所以模块内部互链用相对路径，两端都可用：

```markdown
[Claude Code 配置](../claude-code/index.md)
```

### 跨仓库跳转 → 子仓库的 GitHub blob URL

父仓库的 git 树里只有 gitlink（`mode 160000`），**不存在**子仓库的文件路径，
因此跨仓库写成相对路径在 GitHub 上必然 404。这类链接统一写成子仓库的 blob URL：

```markdown
[实用工具推荐](https://github.com/huluhuluu/useful-tools/blob/main/index.md)
```

`layouts/_markup/render-link.html` 会识别这种 URL，构建时改写成站内永久链接
（上例 → `/p/useful-tools/`），所以：

- **GitHub 上**：直接跳到子仓库对应文件，能读到源码
- **站点上**：改写为站内链接，读者留在站内

> 新增子模块时，需同步更新 `render-link.html` 顶部的 `$ghMap`
> （仓库名 → 目录名 / 挂载点），以及 `hugo.toml` 里的 `module.mounts`。

## 本地开发

### 环境要求

- Hugo Extended (v0.155.3+)
- Dart Sass
- Git

### 快速开始

```bash
# 克隆仓库及子模块
git clone --recursive https://github.com/huluhuluu/MyBlog.git

# 或分步克隆
git clone https://github.com/huluhuluu/MyBlog.git
cd MyBlog
git submodule update --init --recursive

# 本地预览
hugo server -D
```

## 部署

博客自动部署到 Vercel，推送代码后自动触发构建。

## 许可证

博客内容采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可证。
