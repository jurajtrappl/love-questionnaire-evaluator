from functools import reduce


class GoogleForm:
    """
    Represents a wrapper around the Google Form object.
    """

    def __init__(self, form_id, service):
        self.__form_id = form_id
        self.__service = service

    def retrieve_form_responses(self):
        """
        Retrieve all form responses for a form with the given id.

        Args:
            service - Google Forms API service.
            form_id - identification number of the form for which to retrieve the responses.

        Returns:
            Collection of form responses.
        """

        result = self.__service.forms().responses().list(formId=self.__form_id).execute()

        return result['responses']

    def get_questions_in_order(self):
        """
        Retrieve questions ids in order that they appear in the form.

        Args:
            service - Google Forms API service.

        Returns:
            List of question ids.
        """

        def add_question_id(current_ids, question):
            return current_ids + [question['questionItem']['question']['questionId']]

        result = self.__service.forms().get(formId=self.__form_id).execute()
        valid_questions = filter(
            lambda item: 'questionItem' in item, result['items'])

        return reduce(add_question_id, valid_questions, [])
