# Summary
Refine README with additional examples, use cases for agent prompts, and structure clarifications.

## Changes
- Expanded README with detailed use cases for system prompts and sub-agent construction.
- Confirmed and documented storage of all prompts/instructions in isolated `skills/` directories.
- Updated structure sections and removed redundant scope statement.
- Enhanced Contributing guidance for clarity.

## Rationale & Tradeoffs

**Options Considered**
1. Comprehensive README expansion (chosen) - Provides immediate onboarding value with concrete examples while keeping the template focused.
2. Minimal changelog-only update - Insufficient for discoverability.

**Evaluation Matrix**

| Criterion | Weight | Comprehensive Expansion | Minimal Update | Notes |
|-----------|--------|--------------------------|----------------|-------|
| Onboarding Value | High | Excellent | Poor | Examples drive adoption |
| Scope Adherence | High | Maintained | Maintained | No bloat added |
| Discoverability | Med | Improved | Neutral | Use cases attract users |

**Decision Justification**
Prioritizing actionable examples accelerates user ability to store/version/test/refine prompts and skills, directly fulfilling the project's core priority. Tradeoffs favor clarity over brevity for a template repo.

## References
### Issues
N/A

### Acceptance Criteria
- README includes agent/sub-agent examples
- Structure decisions clearly documented
- No scope creep

### Tests
- Manual verification of README rendering
- Consistent with prior skill isolation decisions

### Other
Vercel `npx skills` compatibility preserved; Python DeepEval integration unchanged.

## Lessons & Best Practices
- Templates benefit from concrete, domain-agnostic examples (agent prompts) to demonstrate extensibility without domain-specific bloat.
- Always re-evaluate structure against core priority before documentation updates.
- Changelog entries enforce decision transparency for long-term maintainability.