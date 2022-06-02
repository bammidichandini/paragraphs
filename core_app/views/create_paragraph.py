import json

from django.core.exceptions import BadRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateParagraph(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        from core_app.interactor.create_paragraph import CreateParagraph
        from core_app.storage.paragraphs import ParagraphStorage

        text = json.loads(request.body)

        interactor = CreateParagraph(storage=ParagraphStorage())

        interactor.create_paragraph(text=text)

        return Response("Created")

