from django.contrib import admin

# Register your models here.
from core_app.models import Paragraph, Word

admin.site.register(Paragraph)
admin.site.register(Word)
