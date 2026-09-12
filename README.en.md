# Lingjiang Skill — short-video ideas and expandable outlines

[中文](README.md)

A reusable text-development skill for one short video at a time. Start with materially different angles, compare the reasons people might watch, then develop an outline the creator can fill with their own experience and voice. A full script is written only when explicitly requested. Account strategy, creator-business planning, batch clip libraries, hands-on editing, finished-video review and performance analysis belong to their respective workflows. The name is a project brand, not a requirement to follow one creator's style or business.

Current method version: **0.5.2**. This release tightens delivery-state and routing boundaries and adds reproducible Chinese spoken-duration arithmetic. Existing P0 factual-fidelity failures remain documented and were intentionally outside this maintenance pass.

## Quick start

Download [the standalone Markdown](https://raw.githubusercontent.com/RRR666888000/skills/main/dist/lingjiang-content.md), attach it to an agent that can read the whole file, and ask:

> Use the attached Lingjiang Skill. My confirmed material is […]. I want a […]-second [talking-head / voice-over / on-screen-text] video for […]. Compare a few distinct angles, recommend one, and develop a concrete outline I can expand myself. Do not invent missing events.

For a native skill host, download [the skill ZIP](https://raw.githubusercontent.com/RRR666888000/skills/main/dist/lingjiang-content.zip). Its root contains `SKILL.md` and the required references. Extract it into a `lingjiang-content` folder in your host's supported skill directory. Claude Code uses `.claude/skills/lingjiang-content` (project) or `~/.claude/skills/lingjiang-content` (personal); invoke `/lingjiang-content`. WorkBuddy supports importing a local skill package. See [installation details](docs/INSTALL.md), including Codex, updates and removal.

The core instructions are Chinese. Multilingual agents can follow a request in another language; language quality still depends on the model. Markdown portability is not certification of every host or model. Tests and failures are recorded in [tests](tests/README.md).

The skill covers single-video ideation, expandable outlines, explicitly requested scripts, local revisions and evidence-based audience hypotheses. It locks one delivery state so an outline does not silently become a full script, shot list or publishing package. The method rejects guarantees of virality, invented demographics and fabricated experiences. Models can still violate these instructions; see the observed reliability limit below. Different viewpoints, quiet scenes, commercial work, fiction and non-commercial projects can use different methods.

No paid service, API key, private course or other skill is required for content work. Python 3.9+ is optional when the directory package uses its deterministic duration estimator; without it, the agent must label timing as a rough estimate. Its default character-rate model is for Chinese-dominant speech; English-heavy or mixed-language copy requires a calibrated unit count or a recording. `agents/openai.yaml` is optional host metadata. The repository's MIT license does not license third-party source works. [Sources and boundaries](references/sources.md).

## Observed reliability limit

Claude Code native discovery works in the recorded environment, but its configured `kimi-k2.6` model failed multiple sparse factual-material cases, inventing details, personal reactions or invalid reasoning rules. This is not an Anthropic-model test. Check factual claims before use; reading a package does not certify model behavior. See the complete [test record](tests/README.md).
