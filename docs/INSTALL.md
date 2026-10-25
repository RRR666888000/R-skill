# 安装与更新

需要 Node.js 22.20 或更高版本。[skills CLI](https://github.com/vercel-labs/skills) 会把仓库根目录的 `SKILL.md` 装成技能 `lingjiang-content`，`modules/live-ops` 随这一份技能一起安装。

安装：

```bash
npx skills add RRR666888000/R-skill
```

更新：

```bash
npx skills update lingjiang-content
```

更新命令会同时检查当前项目和全局安装。装到所有项目可用时，安装命令加上 `-g`。
