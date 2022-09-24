from functools import reduce

from das import DasEvaluator
from stls import StlsEvaluator


class ResponseProcessor:
    """
    Process a response and selects the answers that are important for us.
    """

    def __init__(self, questions_in_order):
        self.__questions_in_order = questions_in_order

    def select_relevant_data(self, response):
        """
        Retrieves the answers from a given response that are relevant to extract.

        Args:
            response - a response to extract the answers from.

        Returns:
            Tuple of extracted answers from the response.
        """

        answers = self.__get_question_answers(
            response, self.__questions_in_order)
        das_answers, stls_answers = answers[10:42], answers[42:87]

        email = response['respondentEmail']
        sex = answers[0]
        has_long_enough_relationship = answers[5]
        has_interest_in_interview = answers[87]

        return email, das_answers, stls_answers, sex, has_interest_in_interview, has_long_enough_relationship

    def __get_question_answers(self, response, questions_in_order):
        """
        Extract answers in order from a response.

        Args:
            response - a response object containing the answers to extract.
            questions_in_order - a list of questions in order by which to extract the answers.

        Returns:
            Collection of response answers for the given response.
        """

        def add_answers_from_single_question(current_answers, question_id):
            question = answers[question_id]
            text_answers = question["textAnswers"]["answers"]
            answer = text_answers[0]["value"]

            return current_answers + [answer]

        answers = response["answers"]

        return reduce(add_answers_from_single_question, questions_in_order, [])


class ResponsesEvaluator:
    """
    Evaluate and return results of responses.
    """

    def __init__(self, questions_in_order, stls_scale_factor):
        self.__processor = ResponseProcessor(questions_in_order)
        self.__stls_scale_factor = stls_scale_factor

    def evaluate(self, responses):
        """
        Evaluates and returns results of responses.

        Args:
            responses - responses to evaluate.

        Returns:
            Rows, in a form of a list of lists, of results.
        """

        return reduce(self.__evaluate_single_response, responses, [])

    def __evaluate_single_response(self, current_results, new_response):
        email, das, stls, sex, has_interest_in_interview, has_long_enough_relationship = self.__processor.select_relevant_data(
            new_response)

        intimacy, passion, loyalty = StlsEvaluator(
            self.__stls_scale_factor).score(stls)
        das = DasEvaluator().score(das)

        return current_results + [email, sex, has_interest_in_interview,
                                  has_long_enough_relationship, intimacy, passion, loyalty, das]
