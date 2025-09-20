from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.



@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)