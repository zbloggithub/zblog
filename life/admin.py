# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import LPost

class postInfo(admin.ModelAdmin):
    list_display = ['title', 'modified_time',  'author']

admin.site.register(LPost, postInfo)
