from deepeval.prompt import Prompt

REASONING_PROMPT = Prompt(
    alias="sample-reasoning-v1",
    text_template="Analyze the query step-by-step and provide a concise, evidence-based answer.\nQuery: {query}"
)