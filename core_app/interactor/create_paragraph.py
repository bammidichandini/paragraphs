from core_app.storage.paragraphs import ParagraphStorage


class CreateParagraph():
    def __init__(self, storage: ParagraphStorage):
        self.storage = storage

    def create_paragraph(self, text: str):
        paragraph_dicts = [
            {
                "paragraph": paragraph,
                "words": paragraph.split(" ")
            }
            for paragraph in text.split("\n")
        ]
        self.storage.create_paragraph(paragraph_dicts)

