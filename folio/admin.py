from django.contrib import admin
from .models import Folio


@admin.register(Folio)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["folio_name"]


    class Meta:
        model = Folio