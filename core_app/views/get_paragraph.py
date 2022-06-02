import json

from django.core.exceptions import BadRequest
from django.http import HttpResponse


def get_paragraph(request):
    from core_app.interactor.get_paragraph import GetParagraph
    from core_app.storage.paragraphs import ParagraphStorage

    if request.method != 'POST':
        raise BadRequest()

    word = json.loads(request.body)

    interactor = GetParagraph(storage=ParagraphStorage())

    response = interactor.get_paragraph(word=word)

    return HttpResponse(json.dumps(response))
