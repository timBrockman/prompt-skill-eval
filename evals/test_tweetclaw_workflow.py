import re

import pytest

from skills.tweetclaw_workflow.prompts import TWEETCLAW_WORKFLOW_PROMPT


def test_tweetclaw_prompt_keeps_write_actions_approval_gated():
    prompt = TWEETCLAW_WORKFLOW_PROMPT.text_template.lower()

    assert "approval-gated actions" in prompt
    assert "post tweets" in prompt
    assert "post tweet replies" in prompt
    assert "direct messages" in prompt
    assert "media upload" in prompt
    assert "account-changing" in prompt


def test_tweetclaw_prompt_covers_source_collection_jobs():
    prompt = TWEETCLAW_WORKFLOW_PROMPT.text_template.lower()

    expected_jobs = [
        "scrape tweets",
        "tweet scraper",
        "search tweets",
        "search tweet replies",
        "follower export",
        "user lookup",
        "media download",
        "monitor tweets",
        "webhooks",
        "giveaway draw",
    ]

    for job in expected_jobs:
        assert job in prompt


def test_tweetclaw_prompt_preserves_secret_and_runtime_boundaries():
    prompt = TWEETCLAW_WORKFLOW_PROMPT.text_template

    assert "{objective}" in prompt
    assert "{available_credentials}" in prompt
    assert "{risk_tolerance}" in prompt
    assert "@xquik/tweetclaw" in prompt
    assert "OpenClaw plugin" in prompt
    assert re.search(r"API keys, cookies,\s*tokens, or secret values", prompt)
    assert "agent responsible for scoring, drafting, scheduling, publishing" in prompt
