import json

from django.core.exceptions import BadRequest
from django.http import HttpResponse


def create_paragraph(request):
    from core_app.interactor.create_paragraph import CreateParagraph
    from core_app.storage.paragraphs import ParagraphStorage

    if request.method != 'POST':
        raise BadRequest()

    text = json.loads(request.body)

    interactor = CreateParagraph(storage=ParagraphStorage())

    interactor.create_paragraph(text=text)

    return HttpResponse("Created")

