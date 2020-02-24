from pypandoc import convert_file
from summarizer import top_sentence


NUM_LINES_SUMMARY = 5


class Document:

    def __init__(self, name):

        self.name = name
        self.summary = []

    def get_text(self):

        output = convert_file(self.name, 'txt')
        return output

    def mk_summary(self, n):

        text = self.get_text()
        self.summary = top_sentence(text, n)

    def summarize(self):

        if self.summary == []:
            self.mk_summary(self, NUM_LINES_SUMMARY)

        return '.'.join(self.summary)








