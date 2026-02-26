---
title: "小工具"
date: 2026-01-30T08:00:00+08:00
lastmod: 2026-02-26T18:00:00+08:00
draft: false
description: "开发过程中用到的一些实用小工具配置记录"
slug: "useful-tools"
tags: ["VSCode", "Copilot", "Claude Code", "iFlow"]
categories: ["技术记录"]
comments: true
---

## 1.1 copilot (ui模式 & 第三方api)

`copilot chat`在本地运行可以用本地局域网的一些大模型推理api接口。通过设置ui模式决定让对应插件运行在服务器/本地。
**注意：按需配置**

- `ctrl+shift+p`打开命令面板搜索并且选中`Preferences: Open User Settings (JSON)`。 这将打开本地的vscode设置文件 `settings.json`。

- 在本地settings.json文件中添加extensionKind参数([参数文档](https://code.visualstudio.com/api/advanced-topics/extension-host)), 添加需要本地运行的插件。
```json
"remote.extensionKind": {
	"johnny-zhao.oai-compatible-copilot" : [ // 给copilot-chat配置自定义api接口的插件
		"ui"
	],
	"github.copilot" : [ // copilot
		"ui"
	],
	"github.copilot-chat": [ // copilot chat
		"ui"
	]
}
  ```

  这里插件id可以在插件商店选中插件右键复制
  ![复制插件ID](images/copy-extension-id.png)

- `copilot chat`可以通过插件与其它自行购买**第三方**的api兼容。例如，在VSCode安装`OAI Compatible Provider for Copilot`插件, [仓库链接](https://github.com/JohnnyZ93/oai-compatible-copilot)，可以直接在vscode的插件商店下载。
  ![安装插件](images/install-extension.png)

- 配置`OAI Compatible Provider for Copilot`，接入第三方api，下面以ModelScope社区的api接口为例：

  - 在ModelScope社区的 个人主页->访问控制 里新建一个访问令牌，

  ![新建令牌](images/create-token.png)

  - 随后在模型库搜索需要的模型，支持推理api的就是可以使用api调用的模型，
    ![搜索模型](images/search-model.png)

  - 点击这个模型，进入这个模型的描述页面，右侧有api调用的接口，存在不同格式，按需选择。
    ![模型详情](images/model-details.png)

  - 查看代码范例，中有该模型接口的 的base_url 和 模型id信息
    ![API信息](images/api-info.png)

  - 配置插件信息，`ctrl+shift+p` 命令行搜索打开`OAICopilot: Open Configuration UI`
    
    添加供应方(provider): 需要填写baseurl(上面出现的base_url)和token(前面新建的访问令牌)，以及对应的api接口格式，例如OpenAI格式(这里是查看代码范例时选择的格式)

    ![配置Provider](images/config-provider.png)
    
    ![填写Provider信息](images/fill-provider.png)
    
    添加模型 需要填写前面添加的provider(可以自定义)和模型id(上面出现的模型id)
    ![配置模型](images/config-model.png)
    
    ![填写模型信息](images/fill-model.png)

    目前插件支持openai,openai-responses,ollama,anthropic,gemini等多种格式，具体细节见[插件仓库](https://github.com/JohnnyZ93/oai-compatible-copilot)。
    
	每个模型可以定义采样的temperature top_p top_k等参数，细节同见[仓库]((https://github.com/JohnnyZ93/oai-compatible-copilot)
    
  - 在copilot chat界面选择对应模型 就可以使用对应模型的copilot chat了
    ![选择模型](images/select-model.png)

## 1.2 flash.vscode

使用[flash.vscode](https://github.com/dautroc/flash-vscode)插件可以在vscode中跳转到屏幕可见的任意一行

- 直接在vscode插件商店下载`flash.vscode`插件
	![下载插件](images/download-flash.png)

- `ctrl+shift+p`面板搜索选择`flash-vscode: Start Navigation`，然后键入光标想去的位置的单词，例如下面我输入的是llm
	![输入关键词](images/input-keyword.png)

	屏幕中所有可见的llm都被索引到 并且后方出现一个字母标签，按下对应的字母标签 光标就可以跳转到对应位置，例如按下位置c, 光标出现在左边分屏的第265行
	![跳转效果](images/jump-result.png)

- 绑定快捷键：现在的启动方式还是太抽象了，`ctrl+shift+p`面板搜索选择`Preferences: Open Keyboard Shortcuts (JSON)`, 添加快捷键绑定，现在可以通过"ctrl"和";"启动搜索。**注意这个启动命令可能随着插件版本升级更换，具体命令见[GitHub仓库](https://github.com/dautroc/flash-vscode)**。
	```json
	    {
	        "key": "ctrl+;",
	        "command": "flash-vscode.start" // 可能更换
	    }
	```

- 取消这次搜索按ESC键

## 1.3 claude code

[claude code](https://github.com/anthropics/claude-code)是anthropic推出的一个本地运行的agent框架，可以接入claude或者兼容claude的第三方模型，支持工具使用和技能配置。下面是**Ubuntu 22.04系统**的安装配置记录：

- 第一步，下载安装`claude code`(需要魔法, [参考安装教程](https://www.runoob.com/ai-agent/claude-code.html))，并且为了使用第三方api需要禁用登录。
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  
  vim ~/.claude.json
  # 添加/修改下面内容为
  # "hasCompletedOnboarding": true // 禁用登录
  
  # 如果已经使用cluade需要清理一下~/.claude.json的备份
  # rm -rf ~/.claude.json.*
  ```

- 第二步，安装`cc-switch`，这是一个可以在`claude code`中同时管理并且切换不同的大模型api，支持claude和兼容claude的第三方模型。**注意：如果只使用claude官方模型可以跳过这一步**
  - [选择对应的cli版本](https://github.com/SaladDay/cc-switch-cli)，下面具体获取的包需要在[release界面获取](https://github.com/SaladDay/cc-switch-cli/releases)，优先获取musl静态编译版。
	```bash
	# 下载
	curl -LO https://github.com/SaladDay/cc-switch-cli/releases/download/v4.5.0/cc-switch-cli-v4.5.0-linux-x64-musl.tar.gz
	
	tar -xzf cc-switch-cli-*.tar.gz # 解压
	rm cc-switch-cli-*.tar.gz # 删除压缩包
	chmod +x cc-switch # 执行权限
	sudo mv cc-switch /usr/local/bin/ # 放到系统路径
	```

  - `cc-switch`配置claude api，参考[文档](https://github.com/SaladDay/cc-switch-cli)(有[中文版](https://github.com/SaladDay/cc-switch-cli/blob/main/README_ZH.md))，输入对应的模型提供商、url、模型id、接口令牌等信息就可以了，下面是配置的示例：
	```bash
	➜  cc-switch provider list              # 列出所有供应商
	No providers found.
	Use 'cc-switch provider add' to create a new provider.
	
	➜  ~ cc-switch provider add
	Add New Provider
	==================================================
	> Provider Name: DeepSeek
	> Website URL (optional): 
	Generated ID: deepseek
	
	Configure Claude Provider:
	> API Key: ********************************
	> Base URL: https://api.deepseek.com/anthropic
	> Configure model names? Yes
	> Default Model:： deepseek-chat
	> Haiku Model:： deepseek-chat
	> Sonnet Model:： deepseek-chat
	> Opus Model:： deepseek-chat
	> Configure optional fields (notes, sort index)? Yes
	
	Optional Fields Configuration:
	> Notes: 
	> Sort Index: 
	
	=== Provider Configuration Summary ===
	ID: deepseek
	Provider Name:: DeepSeek
	
	Core Configuration:
	  API Key: sk-0...841d
	  Base URL: https://api.deepseek.com/anthropic
	  Model: deepseek-chat
	======================
	? 
	Confirm create this provider? (y/N) y 
	
	# 再查看就有了
	➜  cc-switch provider list                                     
	┌───┬──────────┬──────────┬────────────────────────────────────┐
	│   ┆ ID       ┆ Name     ┆ API URL                            │
	╞═══╪══════════╪══════════╪════════════════════════════════════╡
	│ ✓ ┆ deepseek ┆ DeepSeek ┆ https://api.deepseek.com/anthropic │
	└───┴──────────┴──────────┴────────────────────────────────────┘
	
	ℹ Application: claude
	→ Current: deepseek # 当前使用的deepseek
	
	# 在打开claude就可以使用了
	➜ claude
	```

	模型的url、id、token令牌等获取同[1.1节](#1.1-copilot-ui-mode--其它模型的copilot-chat兼容), 这里配置的[deepseek模型](https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)，下面是加入claude code的测试结果
	![测试结果](images/test-result.png)

- 第三步，配置skills，可以在开源仓库/社区获取skills，如[官方skills](https://github.com/anthropics/skills)，[Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)，[skillsmp](https://skillsmp.com/)， [skills.sh](https://skills.sh/)等
	```bash
	# skill 包含如下结构， 可以理解为高级提示词 
	# 参考教程: https://support.claude.com/en/articles/12512180-using-skills-in-claude 
	#		   https://www.runoob.com/ai-agent/skills-agent.html 
	
	# 文件结构如下
	# skill-name/
	# ├── SKILL.md          # Required: Skill instructions and metadata
	# ├── scripts/          # Optional: Helper scripts
	# ├── templates/        # Optional: Document templates
	# └── resources/        # Optional: Reference files
	
	# 把下载好的skill放到下面目录就可以在claude code中使用
	# mkdir -p ~/.config/claude-code/skills/
	# cp -r skill-name ~/.config/claude-code/skills/
	
	# 下面以https://skillsmp.com/skills/tldraw-tldraw-claude-skills-write-tbp-skill-md为例
	# 右边有install命令 如下:
	➜  npx skills add tldraw/tldraw # 中间的命令通过方向键 和 空格键 选中
	➜  ls -lah /root/.claude/skills # 可以在skills目录下查找到对应的skills
	total 8.0K
	drwxr-xr-x 2 root root 4.0K Feb  3 19:34 .
	drwxr-xr-x 9 root root 4.0K Feb  3 19:36 ..
	lrwxrwxrwx 1 root root   32 Feb  3 19:34 find-skills -> ../../.agents/skills/find-skills
	lrwxrwxrwx 1 root root   32 Feb  3 19:34 review-docs -> ../../.agents/skills/review-docs
	lrwxrwxrwx 1 root root   34 Feb  3 19:34 skill-creator -> ../../.agents/skills/skill-creator
	lrwxrwxrwx 1 root root   41 Feb  3 19:34 update-release-notes -> ../../.agents/skills/update-release-notes
	lrwxrwxrwx 1 root root   32 Feb  3 19:34 write-docs -> ../../.agents/skills/write-docs
	lrwxrwxrwx 1 root root   36 Feb  3 19:64 write-e2e-tests -> ../../.agents/skills/write-e2e-tests
	lrwxrwxrwx 1 root root   34 Feb  3 19:64 write-example -> ../../.agents/skills/write-example
	lrwxrwxrwx 1 root root   32 Feb  3 19:64 write-issue -> ../../.agents/skills/write-issue
	lrwxrwxrwx 1 root root   30 Feb  3 19:64 write-pr -> ../../.agents/skills/write-pr
	lrwxrwxrwx 1 root root   40 Feb  3 19:64 write-release-notes -> ../../.agents/skills/write-release-notes
	lrwxrwxrwx 1 root root   30 Feb  3 19:64 write-tbp -> ../../.agents/skills/write-tbp
	lrwxrwxrwx 1 root root   37 Feb  3 19:64 write-unit-tests -> ../../.agents/skills/write-unit-tests
	```

  - 测试，第一次使用会询问工具权限，如果不应该使用工具可以附上应该怎么做，例如```Fetch(https://github.com/alibaba/MNN)``` 这一步被取消了 理由是当前目录就在MNN中

	![工具权限](images/tool-permission.png)

## 1.4 iflow

[iflow](https://platform.iflow.cn/)是阿里推出的一个在终端中运行的agent框架，可以接入多种大模型api，目前提供限免的GLM5.0,Kimi-K2.5,MiniMax-M2.5等模型。下面以windows为例，配置记录如下：

- 第一步，安装[nodejs](https://nodejs.org/en/download)，选择对应系统与指令集的预编译安装包，下载后双击，同意协议并安装
	![安装NodeJS](images/install-nodejs.png)

- 第二步，打开powershell安装iflow
	```powershell
	npm install -g @iflow-ai/iflow-cli@latest
	iflow --version # 有输出验证安装成功
	```

- 第三步，登录，打开powershell，启动iflow后进入登录界面
	```powershell
	iflow
	```
	共有三个登录方式：
	1是打开网页授权；2是使用apikey，需要在[心流api平台](https://platform.iflow.cn/profile?tab=apiKey)设置，这个key每周会刷新，过期后可以通过/auth命令刷新；3是使用openai兼容的第三方api

	![登录界面](images/login-page.png)

	配置好key后，可以选择使用的模型，

	![选择模型](images/choose-model.png)

### 1.4.1 小技巧

- `/resume`命令可以恢复之前的对话，继续之前的上下文
- `/clear`命令可以清除之前的对话上下文，重新开始
- `/compress`命令可以压缩之前的对话上下文，保留关键信息，释放上下文空间
- `/init`命令可以初始化一个新的对话，会在目录下生成AGENTS.md文件，记录初始化信息
