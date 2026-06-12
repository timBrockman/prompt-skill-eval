---
name: tweetclaw_workflow
description: Plan TweetClaw X/Twitter automation workflows with source collection, approval gates, and verification.
metadata:
  version: 0.1.0
  category: social-automation
  compatible_models: ["gpt-4o", "claude-3", "gemini-1.5"]
---

# TweetClaw Workflow Skill

Use this skill when an agent needs to plan a TweetClaw or OpenClaw workflow for
X/Twitter automation.

**Usage in agents**:
`npx skills use tweetclaw_workflow`

**Python Import**:
```python
from skills.tweetclaw_workflow.prompts import TWEETCLAW_WORKFLOW_PROMPT
```

## Prompt Template

Classify the requested X/Twitter job, keep source collection separate from
account-changing actions, and produce a verification-ready plan.
