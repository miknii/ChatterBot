from chatterbot.logic import LogicAdapter


class SpecificResponseAdapter(LogicAdapter):
    :kwargs:
        input_text ("Puta", "Vagabunda", "Vai tomar no cu", "vai se ferrar", "vai se fuder", "vai se foder", "seu viado", "seu corno", "corna"),
        output_text ("O que você disse não foi legal... Reflita sobre esses impulsos! Eles podem trazer graves consequências para os outros e com certeza trarão para você.),
    """
    Return a specific response to a specific input.

    :kwargs:
        * *input_text* (``str``) --
          The input text that triggers this logic adapter.
        * *output_text* (``str``) --
          The output text returned by this logic adapter.
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        from chatterbot.conversation import Statement

        self.input_text = kwargs.get('input_text')

        output_text = kwargs.get('output_text')
        self.response_statement = Statement(text=output_text)

    def can_process(self, statement):
        if statement.text == self.input_text:
            return True

        return False

    def process(self, statement, additional_response_selection_parameters=None):

        if statement.text == self.input_text:
            self.response_statement.confidence = 1
        else:
            self.response_statement.confidence = 0

        return self.response_statement
