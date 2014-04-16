#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from django.contrib import admin

from models import *


class AdminTag(admin.ModelAdmin):
    fields = ['name', ]


class AdminQuestion(admin.ModelAdmin):
    #fields = (('name', 'cat'), 'owner','raiting')
    date_hierarchy = 'created'
    list_display = ['name', 'tags_list', 'owner']
    ordering = ['updated']
    readonly_fields = ['raiting', 'slug']
    preserve_filters = True

admin.site.register(Question, AdminQuestion)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(User)
