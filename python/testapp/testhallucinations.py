import os
from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import HallucinationMetric
from deepeval.models import GeminiModel
from chatbot import chatbot

def test_hallucination_metrics():
    input = "what is maximum personal loan i can apply?"
    output = chatbot(input)
    context = [
        "the maximum loan can be provided is 13 milion USD",
        "the arte of interest is 7%", 
        "the maximum number of year allowed is 18 year"
        ]

    #here context is different than main chatbot context so this will fail

    test_case = LLMTestCase(
        input= input,
        actual_output= output,
        context=context

    )

    gemini_judge = GeminiModel(
            model="gemini-3.1-flash-lite",
            api_key=os.getenv("GEMINI_API_KEY")
        )
    hallucination_metric = HallucinationMetric(
        threshold=0.9, 
        model=gemini_judge,

        )
    evaluate([test_case], [hallucination_metric])
    print(output)






