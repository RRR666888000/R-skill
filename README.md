# 凌酱 Skill

[English](README.en.md)

凌酱 Skill（`lingjiang-content`，当前 0.9.0）是交给 AI Agent 的内容技能：把一句想法做成能拍的短视频，并带上灵魂问答和直播运营。

## 短视频创作

从一个零散想法出发，比较不同方向、搭骨架，需要时写全文、改局部，或从受众角度做审计。

## 灵魂问答

说「灵魂问答」即进入。按六组逐组提问，沿用已经给出的信息，做内容调研和获客分析。

## 直播运营

遇到逼单、话术、过款、留人、主播、场观、转化、人货场、PFABES、七词这类直播卡点，就进入直播运营。也可以直接说「开启凌酱直播运营skill」。

## 安装

```bash
npx skills add RRR666888000/R-skill
```

### 没装 Node 怎么办

① 安装 Node：到 [nodejs.org](https://nodejs.org) 下载 LTS，或在 Mac 上运行 `brew install node`。

② 完全不用 Node，用 git。安装：

```bash
git clone https://github.com/RRR666888000/R-skill ~/.agents/skills/lingjiang-content
```

更新：

```bash
cd ~/.agents/skills/lingjiang-content && git pull
```

用 Claude Code 的话，把路径换成 `~/.claude/skills/lingjiang-content`。

## 更新

```bash
npx skills update lingjiang-content
```

需要 Node.js 22.20 或更高版本。说明见 [安装与更新](docs/INSTALL.md)。

## 怎么触发

直接说要做的事：

- 「帮我想几个选题，再推荐一个骨架。」
- 「这篇局部改一下，再从受众角度审一遍。」
- 「陪我走一轮灵魂问答，先做内容调研。」
- 「用户老说再看看，怎么逼单？」
- 「开启凌酱直播运营skill。」

更多说法见 [示例提示词](docs/EXAMPLES.md)。方法边界见 [来源说明](references/sources.md)。反馈请到 [Issues](https://github.com/RRR666888000/R-skill/issues)。[MIT 许可](LICENSE)。
