import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class GetParagraph(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        from core_app.interactor.get_paragraph import GetParagraph
        from core_app.storage.paragraphs import ParagraphStorage

        word = json.loads(request.body)

        interactor = GetParagraph(storage=ParagraphStorage())

        response = interactor.get_paragraph(word=word)

        return Response(json.dumps(response))
