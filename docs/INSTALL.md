# 安装与更新

用 `npx` 安装需要 Node.js 22.20 或更高版本。[skills CLI](https://github.com/vercel-labs/skills) 会把仓库根目录的 `SKILL.md` 装成技能 `lingjiang-content`，`modules/live-ops` 随这一份技能一起安装。

安装：

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

已有 Node 时，更新：

```bash
npx skills update lingjiang-content
```

更新命令会同时检查当前项目和全局安装。装到所有项目可用时，安装命令加上 `-g`。
