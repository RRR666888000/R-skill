# 安装、调用、更新与卸载

这些是供新用户操作的步骤，不代表你的设备已安装。核对日期：2026-09-12。目录位置、权限和菜单由宿主及其版本决定；同一个Skill文件可读，不表示每种模型表现一致。

## 先选交付形式

| 你的Agent能力 | 用哪个文件 |
|---|---|
| 支持导入本地技能包，如WorkBuddy | [技能ZIP](https://raw.githubusercontent.com/RRR666888000/R-skill/main/dist/lingjiang-content.zip)；根目录就是SKILL.md |
| 会扫描本地Skill目录，如Claude Code或Codex | 解压技能ZIP，把内容放进名为lingjiang-content的技能文件夹 |
| 不支持Skill，但能读完整附件或文本 | [通用Markdown](https://raw.githubusercontent.com/RRR666888000/R-skill/main/dist/lingjiang-content.md)；作为本次对话的方法附件 |
| 无法接收方法文件或自定义指令 | 没有通用安装办法，需换可接收方法的入口 |

不要把GitHub“Code → Download ZIP”得到的整仓库直接当导入包。整仓库供浏览源码；`dist/lingjiang-content.zip`才是专用技能包。

## Codex

1. 下载并解压技能ZIP。
2. 创建个人技能目录`~/.codex/skills/lingjiang-content/`，将 ZIP 内全部内容放进去，包括`SKILL.md`、`LICENSE`、`references/`、`agents/`和`scripts/`。`scripts/estimate_duration.py`是可选时长工具，不要漏复制。该路径已在本次本机Codex运行中核验；你的宿主若使用不同配置目录，以实际技能列表为准。
3. 新开会话或刷新技能列表，找到`lingjiang-content`，核对实际路径和启用状态。
4. 发“用凌酱Skill……”或显式使用`$lingjiang-content`。先用文末的小例子验证输出。

不要多嵌套一层成`lingjiang-content/lingjiang-content/SKILL.md`。已有同名技能时先备份，不覆盖自己的修改。

## Claude Code

将解压内容放到个人目录`~/.claude/skills/lingjiang-content/`，或仅当前项目的`.claude/skills/lingjiang-content/`。从该项目启动Claude Code，使用`/lingjiang-content`，也可明确自然语言调用。目录及命令依据[Claude Code官方说明](https://code.claude.com/docs/en/skills)。

项目结构应是：

```text
.claude/skills/lingjiang-content/
  SKILL.md
  references/
    development.md
    ...
  agents/openai.yaml
  scripts/estimate_duration.py
  LICENSE
```

`agents/openai.yaml`可忽略，不是Claude调用依赖。仅有工具说“我用了”不够；检查其实际读取的入口和输出。测试环境与结果见[测试矩阵](../tests/README.md)。本次原生发现实测通过，配置模型`kimi-k2.6`的保真测试未通过；不要把安装成功理解成内容审核通过。

本机Claude Code 2.1.177自动化实测中，`--bare`进入精简模式后跳过了项目Skill发现，即使同时给`--add-dir`也不能据此证明Skill已加载；因此原生Skill行为测试不要使用`--bare`。使用正常隔离会话、`--setting-sources project,local`和显式`/lingjiang-content`，并从调试记录或实际读取确认命令已识别。这个结论只对应所记录版本，其他版本仍须现场核对。`--safe-mode`下直接输入单文件属于文本调用。[官方无头模式说明](https://code.claude.com/docs/en/headless)

## WorkBuddy（腾讯）

在左侧技能入口打开技能管理，选择“添加技能 → 上传技能”，导入`dist/lingjiang-content.zip`。在“已安装”中核对并启用，再在对话中说“使用凌酱Skill，处理下面的短视频素材……”。官方说明提供本地技能包导入与已安装技能调用入口：[WorkBuddy技能](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)、[腾讯云说明](https://cloud.tencent.com/document/product/1831/134432)。不同版本界面可能略有差异。

本次没有WorkBuddy本机运行结果，不能把官方支持ZIP当成这个包已在该宿主实测。若导入失败，先核对ZIP根目录有`SKILL.md`、包内引用齐全，再查看宿主错误。无法导入但能读附件时，可试单文件方式；这属于文本调用，不等于原生安装。

## DeepSeek Harness（官方dsh）

0.5.2的目录结构沿用0.5.1已核对的官方本地Skill规范，未在朋友设备或DSH运行时实测。将技能ZIP解压到项目根目录的`.dsh/skills/lingjiang-content/`，使其直接包含`SKILL.md`和`references/`。个人共享也可用`~/.dsh/skills/lingjiang-content/`；若设置DSH_HOME，以实际目录为准。项目根默认取最近的.git上级目录，没有则用会话工作目录。[官方目录与格式](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md)

使用带Skills的标准模式，或确认自定义模式启用了Skill目录与加载能力；极简模式不可假定提供该入口。[官方模式说明](https://www.deepseek.com/harness/)

在对应工作区调用：

```text
/lingjiang-content 我的素材是……。给三个不同方向，推荐一个骨架，我自己续写。
```

也可自然语言明确要求使用lingjiang-content。原生调用应能找到名称、加载当前入口并按需读取相对参考；此包名称、描述、metadata、默认调用权限与显式参考路径符合文档，不需要安装成运行时插件。[调用说明](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/README.md)、[参考文件解析](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md)

若找不到，检查工作区、同名覆盖、目录是否多套一层及模式是否启用Skills。仅上传无YAML头的通用单文件是文本使用，不等同原生安装。模型行为还需用自己的合成素材核对，Claude Code里配置Kimi的结果不能代表DeepSeek模型。

## Gemini CLI、OpenClaw及其他Agent

- Gemini CLI：将完整文件夹放在`~/.gemini/skills/lingjiang-content/`或项目`.gemini/skills/lingjiang-content/`；官方也支持`.agents/skills`别名。使用`/skills reload`刷新、`/skills list`核对。[官方说明](https://geminicli.com/docs/cli/using-agent-skills/)
- OpenClaw：使用目标工作区`skills/lingjiang-content/`或共享状态目录的`skills/lingjiang-content/`（默认`~/.openclaw/skills/lingjiang-content/`）。确认目标Agent能发现并启用；不同状态配置会改变作用域。[官方说明](https://docs.openclaw.ai/tools/skills)
- 其他文件型Agent：明确让它读`SKILL.md`并按需读相对参考，不猜某种斜杠命令。其他聊天产品上传整份单文件即可试用。

后两者的原生运行未在本次测试；别复制某个产品的命令到所有Agent。

## 交给Agent安装的一句话

> 请检查此仓库的SKILL.md与references，按当前宿主支持的位置安装lingjiang-content。安装前检查同名目录，有旧版先备份，不改全局指令和其他技能。完成后核对文件、引用、实际发现路径与启用状态，再用一个虚构素材验证调用。如果当前产品没有原生技能入口，请改为读取dist/lingjiang-content.md，并明确这是文本调用。仓库：https://github.com/RRR666888000/R-skill

## 四层验收

1. **文件**：入口存在、引用齐全、版本正确，附件完整读入。
2. **发现**：原生宿主能列出技能，核对加载路径、同名覆盖与启用状态；文本附件模式不声明原生发现。
3. **调用**：显式调用时确认本轮确实读取该入口；隐式调用另测，不能因目录可发现就假定自然语言一定会选中。
4. **行为**：发“我有三天同一扇窗的照片，一晴两雨；给两个方向并推荐一个短口播骨架”。应有不同观看任务和具体内容，但不先写完整稿、分镜或发布文案。再用“418个口播单位、每分钟120、另停顿3秒”验证总时长应为212秒。只要求改首句时不重写全篇。

## 更新与卸载

更新前备份同名目录及你自己的修改，再用新版完整目录替换旧文件，刷新/新开会话后核对版本。多个宿主的副本分别更新。不要只换SKILL.md留下旧references；单文件也要整体换新，避免旧上下文干扰。

卸载只移走`lingjiang-content`文件夹（或自己创建的指向它的链接），再刷新技能列表；WorkBuddy可从已安装技能管理移除。不要删除整个`.codex`、`.claude`或`.agents`目录。附件用法另开不含该附件的新对话。

找不到时检查：是不是多嵌套了一层、文件名大小写是否正确、所在位置是否被宿主扫描、是否禁用、是否被同名技能覆盖、当前用的是本地还是云端环境。
