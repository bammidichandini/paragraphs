from typing import Dict, Any, List

from core_app.models import Paragraph, Word


class ParagraphStorage():
    @staticmethod
    def create_paragraph(paragraph_dicts: List[Dict[str, Any]]):
        words_objs = []
        for paragraph_dict in paragraph_dicts:
            paragraph = paragraph_dict["paragraph"]
            words = paragraph_dict["words"]
            paragraph_obj = Paragraph.objects.create(
                content=paragraph)
            for word in words:
                words_objs.append(
                    Word(word=word, paragraph=paragraph_obj))
        Word.objects.bulk_create(objs=words_objs)

    @staticmethod
    def get_paragraph(word: str) -> List[str]:
        paragraph_ids = Word.objects.filter(
            word=word
        ).values_list("paragraph_id", flat=True)

        paragraphs = Paragraph.objects.filter(
            id__in=list(paragraph_ids)).values_list("content")

        return list(paragraphs)
