from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import AboutPage

@admin.register(AboutPage)
class AboutPageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


