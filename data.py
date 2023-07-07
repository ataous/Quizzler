import requests

from question_model import Question

API_URL = "https://opentdb.com/api.php"


def get_question_from_api() -> list[dict[str, str | list[str]]]:
    """
    Get Data From opentdb API
    :return: [{'category': 'string',
             'type': 'string',
             'difficulty': 'string',
             'question': 'string',
             'correct_answer': 'string',
             'incorrect_answers': ['string']
             }]
    """
    parameters = {
        "amount": 10,
        "category": 18,
        "type": "boolean"
    }
    response = requests.get(API_URL, params=parameters)
    response.raise_for_status()
    return response.json()["results"]


def get_question_bank() -> list[Question]:
    """
    Call get_question_from_api fun and return list of question
    :return: list[Question]
    """
    question_data = get_question_from_api()
    result = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        result.append(new_question)
    return result


question_bank = get_question_bank()
