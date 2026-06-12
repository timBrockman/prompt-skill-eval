from deepeval.prompt import Prompt

TWEETCLAW_WORKFLOW_PROMPT = Prompt(
    alias="tweetclaw-workflow-v1",
    text_template=(
        "Plan a TweetClaw X/Twitter automation workflow.\n"
        "Objective: {objective}\n"
        "Available credentials or approvals: {available_credentials}\n"
        "Risk tolerance: {risk_tolerance}\n\n"
        "Classify each requested action before drafting the plan:\n"
        "- Source collection: scrape tweets, tweet scraper jobs, search tweets, "
        "search tweet replies, follower export, user lookup, media download, "
        "monitor tweets, webhooks, and giveaway draw evidence collection.\n"
        "- Approval-gated actions: post tweets, post tweet replies, direct "
        "messages, media upload, monitor creation, webhook creation, and any "
        "account-changing X/Twitter automation.\n\n"
        "Use TweetClaw only as the execution or evidence source. Keep the "
        "agent responsible for scoring, drafting, scheduling, publishing, "
        "analytics, and control decisions. Do not expose API keys, cookies, "
        "tokens, or secret values in commands or output. Prefer the canonical "
        "package @xquik/tweetclaw and the TweetClaw OpenClaw plugin when an "
        "agent runtime is available.\n\n"
        "Return four sections: classification, approval_required, workflow, "
        "and verification. The workflow must name the concrete user jobs it "
        "supports, including MCP, OpenClaw plugin, and agent tools when they "
        "are relevant."
    ),
)
