# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import SPost, SCategory, STag

class CategoryInfo(admin.ModelAdmin):
    list_display = ['name']

class TagInfo(admin.ModelAdmin):
    list_display = ['name']

class postInfo(admin.ModelAdmin):
    list_display = ['title', 'modified_time', 'category', 'author']

admin.site.register(SPost, postInfo)
admin.site.register(SCategory, CategoryInfo)
admin.site.register(STag, TagInfo)
