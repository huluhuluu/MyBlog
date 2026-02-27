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
| `content/post/mnn-tutorial` | MNN 端侧部署教程 |
| `content/post/leetcode-logs` | LeetCode 刷题记录 |

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
