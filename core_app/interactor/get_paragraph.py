from core_app.storage.paragraphs import ParagraphStorage


class GetParagraph():
    def __init__(self, storage: ParagraphStorage):
        self.storage = storage

    def get_paragraph(self, word: str):
        paragraphs = self.storage.get_paragraph(word)

        return paragraphs

