# prompt-skill-eval

Modular, testable prompt and agent skill library with **DeepEval** metrics, multi-model GitHub Actions CI, and full **Vercel `npx skills`** compatibility.

## Features
- Per-skill directories with `SKILL.md` (Vercel discovery) + Python `deepeval.prompt.Prompt` registry
- Rigorous pytest + DeepEval test suites with custom G-Eval metrics
- Multi-model matrix testing (OpenAI, Anthropic, Gemini, etc.)
- Automated CI with pass/fail gating on push/PR
- Easy consumption: path imports, copy-paste, or `pip install -e`

## Quick Start

```bash
git clone https://github.com/timBrockman/prompt-skill-eval.git
cd prompt-skill-eval
pip install -e .
pip install -r requirements.txt

# Run evaluations
deepeval test run evals/test_sample_skill.py
```

## Adding a New Skill
1. Copy `skills/sample_skill/` template.
2. Update `SKILL.md` frontmatter and instructions.
3. Implement prompts in `prompts.py` and tests in `evals/`.
4. CI will validate automatically.

This library challenges ad-hoc prompt management by enforcing executable quality from day one.

**License**: MIT
