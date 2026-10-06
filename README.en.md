# Lingjiang Skill — short-video ideas and expandable outlines

[中文](README.md)

A reusable text-development skill for one short video at a time. Start with materially different angles, compare the reasons people might watch, then develop an outline the creator can fill with their own experience and voice. A full script is written only when explicitly requested. Account strategy, creator-business planning, batch clip libraries, hands-on editing, finished-video review and performance analysis belong to their respective workflows. The name is a project brand, not a requirement to follow one creator's style or business.

Current method version: **0.8.0**. Restores article procedures and the user-requested interactive workflow lost in 0.7.0. The six verbatim prompts are unchanged. Additional AI task descriptions, the author's filled business example, sampling, keywords, same-industry templates and correction against real buyer data are now included, with original excerpts separated from execution instructions.

## Soul Questions subfeature

Say “灵魂问答” (Soul Questions) with a topic. The agent uses known inputs, asks one group at a time, and performs the corresponding analysis after the user's answer. Original quantities remain required; a narrower scope requires an explicit user request. Missing evidence is reported rather than fabricated.

Read [the original prompts](references/soul-questions.md), [the full AI-instruction inventory](references/soul-prompt-inventory.md), [verbatim article context](references/soul-source-context.md), and [the execution workflow](references/soul-workflow.md). The latter distinguishes article-derived procedures from user-requested interaction and business adaptation. The author's B2B example must not cause a consumer-product business to reject its own buyers as irrelevant.

These files are bundled in the directory, ZIP and standalone Markdown. Remove superseded official `references/soul-delivery.md` and `references/soul-research.md` when upgrading, preserving local custom edits separately. Ordinary video rules and historical fidelity failures remain unchanged. See [0.8.0 checks](tests/soul-080/README.md); older Soul Questions records describe prior versions.

## Download for people

- **Try without installing:** download [the complete Markdown file](https://raw.githubusercontent.com/RRR666888000/R-skill/main/dist/lingjiang-content.md), save it as `.md`, and attach it to an AI that can read the whole file.
- **Install a skill:** download [the skill ZIP](https://raw.githubusercontent.com/RRR666888000/R-skill/main/dist/lingjiang-content.zip). Import it through your host's skill manager, or extract all its contents into a supported folder named `lingjiang-content`. Keep `SKILL.md`, `references/`, `scripts/`, `agents/` and `LICENSE`. See [host-specific instructions](docs/INSTALL.md).
- **Browse or modify the source:** download [the repository ZIP](https://github.com/RRR666888000/R-skill/archive/refs/heads/main.zip). This is different from the importable skill ZIP.

The repository name is `R-skill`; the installed skill folder and invocation name remain `lingjiang-content`.

## Download and install with an Agent

Copy this request to an Agent that can access the network and files:

```text
Download and install lingjiang-content from https://github.com/RRR666888000/R-skill.
Read https://raw.githubusercontent.com/RRR666888000/R-skill/main/docs/INSTALL.md first.
Download https://raw.githubusercontent.com/RRR666888000/R-skill/main/dist/lingjiang-content.zip
and https://raw.githubusercontent.com/RRR666888000/R-skill/main/dist/manifest.json.
Verify the ZIP SHA-256 and the extracted skill_files against the manifest.
Confirm the current host's supported skill location. Install the complete contents
in a folder named lingjiang-content with SKILL.md directly inside it.
Back up any existing installation and preserve my edits.
Report the actual path, version, file verification and host discovery status.
Test invocation with fictional material where possible; disclose any refresh needed.
Do not describe installation in a cloud sandbox as installation on my computer.
If the host has no native skill support, read the complete standalone file at
https://raw.githubusercontent.com/RRR666888000/R-skill/main/dist/lingjiang-content.md
and identify this as text-based use for the conversation.
If network or file access is unavailable, state the specific missing capability.
```

Public downloads require no repository-specific key. Agents with Git can also clone `https://github.com/RRR666888000/R-skill.git`; cloning alone does not install or enable the skill.

## First request

> Use Lingjiang Skill. My confirmed material is […]. I want a […]-second [talking-head / voice-over / on-screen-text] video for […]. Compare a few distinct angles, recommend one, and develop a concrete outline I can expand myself. Do not invent missing events.

The core instructions are Chinese. Multilingual agents can follow a request in another language; language quality still depends on the model. Markdown portability is not certification of every host or model. Tests and failures are recorded in [tests](tests/README.md).

The skill covers single-video ideation, expandable outlines, explicitly requested scripts, local revisions and evidence-based audience hypotheses. It locks one delivery state so an outline does not silently become a full script, shot list or publishing package. The method rejects guarantees of virality, invented demographics and fabricated experiences. Models can still violate these instructions; see the observed reliability limit below. Different viewpoints, quiet scenes, commercial work, fiction and non-commercial projects can use different methods.

No paid service, API key, private course or other skill is required for content work. Python 3.9+ is optional when the directory package uses its deterministic duration estimator; without it, the agent must label timing as a rough estimate. Its default character-rate model is for Chinese-dominant speech; English-heavy or mixed-language copy requires a calibrated unit count or a recording. `agents/openai.yaml` is optional host metadata. The repository's MIT license does not license third-party source works. [Sources and boundaries](references/sources.md).

## Observed reliability limit

Claude Code native discovery works in the recorded environment, but its configured `kimi-k2.6` model failed multiple sparse factual-material cases, inventing details, personal reactions or invalid reasoning rules. This is not an Anthropic-model test. Check factual claims before use; reading a package does not certify model behavior. See the complete [test record](tests/README.md).

