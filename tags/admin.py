from django.contrib import admin
from . import models
from .models import Tag
# Register your models here.

# admin.site.register(Tag)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']
