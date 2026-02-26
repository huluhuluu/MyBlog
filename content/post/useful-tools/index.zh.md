---
title: "小工具收集"
date: 2026-01-30T08:00:00+08:00
lastmod: 2026-02-25T18:00:00+08:00
draft: false
description: "开发过程中用到的一些实用小工具配置记录"
slug: "useful-tools"
tags: ["VSCode", "Copilot", "Claude Code", "iFlow"]
categories: ["技术记录"]
comments: true
---

## 1.1 copilot ui模式 & 其它模型的copilot chat兼容

copilot chat在本地运行可以用本地局域网的一些api接口。可以通过设置ui模式决定让对应插件运行在服务器/本地。**！！按需配置**

- ctrl+shift+p面板搜索打开Preferences: Open User Settings (JSON)。 如果希望设置成默认可以选择配置Preferences: Open Default Settings (JSON)

- 在本地settings.json文件中添加extensionKind参数，[文档](https://code.visualstudio.com/api/advanced-topics/extension-host)
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
  ![复制插件ID](images/image-20260130084608569.png)

- copilot chat可以通过插件与其它自行购买的api兼容。在VSCode安装OAI Compatible Provider for Copilot插件, [仓库链接](https://github.com/JohnnyZ93/oai-compatible-copilot)
  ![安装插件](images/image-20260130084854531.png)

- 配置OAI Compatible Provider for Copilot，

  - 以ModelScope社区的api接口为例，在个人主页->访问控制 里新建一个访问令牌，

  ![新建令牌](images/image-20260130090658146.png)

  - 在模型库搜索需要的模型，支持推理api的就是可以使用的模型，
    ![搜索模型](images/image-20260130090858573.png)

  - 点击这个模型 进入这个模型的描述页面，右侧有api调用的接口，存在不同格式，按需选择。
    ![模型详情](images/image-20260130091119069.png)

  - 查看代码范式 中有api 和 id信息
    ![API信息](images/image-20260130091604481.png)

  - 配置插件信息，ctrl+shift+p 命令行搜索打开"OAICopilot: Open Configuration UI"
    
    添加供应方(provider) 需要填写baseurl和token

    ![配置Provider](images/image-20260130105337808.png)
    
    ![填写Provider信息](images/image-20260130105608712.png)
    
    添加模型 需要填写前面添加的provider和模型id
    
    ![配置模型](images/image-20260130105817459.png)
    
    ![填写模型信息](images/image-20260130105759267.png)

    目前插件支持openai,openai-responses,ollama,anthropic,gemini格式，具体细节见[插件仓库](https://github.com/JohnnyZ93/oai-compatible-copilot)。
    每个模型可以定义temperature top_p top_k等参数，细节同见[仓库]((https://github.com/JohnnyZ93/oai-compatible-copilot)
    
  - 在copilot chat界面选择对应模型 就可以使用对应模型的copilot chat了
    ![选择模型](images/image-20260130091810839.png)

## 1.2 flash.vscode

使用[flash.vscode](https://github.com/dautroc/flash-vscode)可以在vscode中跳转到屏幕可见的任意一行

- 直接在vscode插件商店下载
	![下载插件](images/image-20260203164114891.png)

- ctrl+shift+p面板搜索选择flash-vscode: Start Navigation，然后键入光标想去的位置的单词，例如下面我输入的是llm
	![输入关键词](images/image-20260203164319035.png)

	屏幕中所有可见的llm都被索引到 并且后方出现一个字母标签，接着按下对应的字母标签光标就可以跳转到对应位置，例如按下位置c, 光标出现在左边分屏的第265行
	![跳转效果](images/image-20260203164417695.png)

- 绑定快捷键：现在的启动方式还是太抽象了，ctrl+shift+p面板搜索选择Preferences: Open Keyboard Shortcuts (JSON), 添加快捷键绑定，现在可以通过"ctrl"和";"启动搜索。**注意这个启动命令可能更换，具体命令见[GitHub仓库](https://github.com/dautroc/flash-vscode)**。
	```json
	    {
	        "key": "ctrl+;",
	        "command": "flash-vscode.start" // 可能更换
	    }
	```

- 取消这次搜索按ESC键

## 1.3 claude code

- 安装claude, 需要魔法。参考教程: [官方仓库](https://github.com/anthropics/claude-code) [菜鸟教程](https://www.runoob.com/ai-agent/claude-code.html) 
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  
  vim ~/.claude.json
  # 添加下面内容
  # "hasCompletedOnboarding": true // 禁用登录
  
  # 如果已经使用cluade需要清理一下~/.claude.json的备份
  # rm -rf ~/.claude.json.*
  ```

- 安装cc-switch，[选择的cli版本](https://github.com/SaladDay/cc-switch-cli)，下面具体获取的包需要在[release界面获取]()，优先获取musl静态编译版。
	```bash
	# 下载
	curl -LO https://github.com/SaladDay/cc-switch-cli/releases/download/v4.5.0/cc-switch-cli-v4.5.0-linux-x64-musl.tar.gz
	
	tar -xzf cc-switch-cli-*.tar.gz # 解压
	rm cc-switch-cli-*.tar.gz # 删除压缩包
	chmod +x cc-switch # 执行权限
	sudo mv cc-switch /usr/local/bin/ # 放到系统路径
	```

- cc-switch配置claude api，参考[仓库文档](https://github.com/SaladDay/cc-switch-cli)(有[中文版](https://github.com/SaladDay/cc-switch-cli/blob/main/README_ZH.md))
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

	api、token等获取同[1.1节](#1.1-copilot-ui-mode--其它模型的copilot-chat兼容), 这里配置的[deepseek模型https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)，下面是加入claude code的测试结果
	![测试结果](images/image-20260203190036967.png)

- 配置skills，可以在开源仓库/社区获取skills，如[官方skills](https://github.com/anthropics/skills)，[Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)，[skillsmp](https://skillsmp.com/)， [skills.sh](https://skills.sh/)等
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

	![工具权限](images/image-20260203195134730.png)

## 1.4 iflow

介绍iflow，下面以windows为例

- 安装[nodejs](https://nodejs.org/en/download)，选择对应系统与指令集的预编译安装包，下载后双击，同意协议并安装
	![安装NodeJS](images/image-20260225162307041.png)

- 打开powershell安装iflow
	```powershell
	npm install -g @iflow-ai/iflow-cli@latest
	iflow --version # 有输出验证安装成功
	```

- 登录，powershell启动后进入登录界面
	```powershell
	iflow
	```

	1是打开网页授权；2是使用apikey，需要在[心流api平台](https://platform.iflow.cn/profile?tab=apiKey)设置，并且这个key每周会刷新，过期后可以通过/auth命令刷新；3是使用openai兼容的第三方api

	![登录界面](images/image-20260225163235300.png)

	配置好key后，可以选择使用的模型，目前全部限免

	![选择模型](images/image-20260225163456321.png)

	配置环境变量，
	
	```json
	"terminal.integrated.persistentSessionReviveProcess": "never"
	```

### 小技巧

- **使用 /help 查看所有命令**：iflow 提供了丰富的命令，如 `/auth` 刷新认证、`/clear` 清空对话、`/compact` 压缩上下文等
- **使用 Tab 自动补全**：输入部分命令后按 Tab 可以快速补全
- **配置 .iflowignore**：类似 .gitignore，可以指定 iflow 忽略的文件和目录，避免扫描不必要的文件
- **多会话管理**：不同项目可以使用不同的会话，上下文互不干扰
