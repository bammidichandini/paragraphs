from django.db import models

# Create your models here.

from django.db import models


class Paragraph(models.Model):
    content = models.TextField()


class Word(models.Model):
    word = models.TextField()
    paragraph = models.ForeignKey(Paragraph, related_name="word", on_delete=models.CASCADE)
