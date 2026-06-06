import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, GEval
from skills.sample_skill.prompts import REASONING_PROMPT

def test_sample_reasoning():
    prompt = REASONING_PROMPT
    # Example test case
    test_case = LLMTestCase(
        input="What is 2+2?",
        actual_output="The sum of 2 and 2 is 4, derived from basic arithmetic.",
        expected_output="4",
        retrieval_context=["Basic math: 2 + 2 = 4."]
    )
    
    metrics = [
        AnswerRelevancyMetric(threshold=0.85),
        FaithfulnessMetric(threshold=0.9),
        GEval(name="Conciseness", criteria="Response is brief, avoids fluff.", threshold=0.8)
    ]
    
    assert_test(test_case, metrics, run_async=False)

if __name__ == "__main__":
    pytest.main([__file__])