import os
from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval
from deepeval.models import GeminiModel
from chatbot import chatbot

def test_answer_relevancy():
    query = "How to apply home loan?"
    output = chatbot(query)
    #output = "Fixed deposite is for fixed deposite token for chatgpt."
    print(output)

    test_case = LLMTestCase(
        input = query,
        actual_output=output
    )

    gemini_judge = GeminiModel(
        model="gemini-3.1-flash-lite",
        api_key=os.getenv("GEMINI_API_KEY")
    )

    #answer_relevancy = AnswerRelevancyMetric(threshold=0.8,model=gemini_judge)
# here you can use Geval instead of answerrelemetric 

    answer_relevancy = GEval(
        name = "answer relevancy",
        criteria="Check if the answer is relevant",
        evaluation_params= [
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT
        ],
        evaluation_steps=[
            "Check if the answer is fully relevant to the query",
            "If the answer is not relevant give the score as 0 if it is fully relevant the give score accordingly"
        ],
        threshold=0.8,
        model=gemini_judge
    )

    result = evaluate([test_case],{answer_relevancy})
    print(result)






