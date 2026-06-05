# prompt-skill-eval

**A great template for storing, versioning, testing, and refining prompts, skills, and instructions.**

Modular, testable prompt and agent skill library with:
- **DeepEval** metrics for rigorous evaluation
- **Vercel `npx skills`** compatibility via `SKILL.md`
- Multi-model GitHub Actions CI/CD
- Versioned, isolated skills for easy reuse across projects

## Features
- **Storage & Versioning**: Git-tracked prompts in Python + SKILL.md metadata
- **Testing**: Pytest + DeepEval with custom G-Eval metrics, threshold gating
- **Refinement**: CI-driven regression detection, multi-model matrix (OpenAI, Anthropic, Gemini, etc.)
- **Reusability**: Path import, pip install -e, or copy-paste. npx skills discovery

## Quick Start
```bash
git clone https://github.com/TimBrockman/prompt-skill-eval.git
cd prompt-skill-eval
pip install -e .
pip install -r requirements.txt
deepeval test run evals/
```

Add new skills by copying `skills/sample_skill/` template.

## Structure
See detailed sections below.

## Contributing
1. Add skill in `skills/<name>/`
2. Write tests in `evals/`
3. PR — CI validates automatically
