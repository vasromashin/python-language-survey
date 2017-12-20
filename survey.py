class AnonymousSurvey():
    """ Collect anonymous answer to a survey questions"""

    def __init__(self, question):
        """Store question and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to a survey"""
        self.responses.append(new_response)

    def show_result(self):
        """Show the responses that have been given"""
        print("Survey results:")
        for response in self.responses:
            print("- {}".format(response))
