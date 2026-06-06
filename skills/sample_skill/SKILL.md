---
name: sample_skill
description: A sample skill demonstrating dual Python + Vercel compatibility. Tests prompt quality via DeepEval.
metadata:
  version: 0.1.0
  category: reasoning
  compatible_models: ["gpt-4o", "claude-3"]
---

# Sample Skill: Concise Reasoning

**Usage in agents**:
`npx skills use sample_skill`

**Python Import**:
```python
from skills.sample_skill.prompts import REASONING_PROMPT
```

## Prompt Template
Concise, evidence-based response to query.