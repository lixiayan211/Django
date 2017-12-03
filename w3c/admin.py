# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CityGallery

# Register your models here.
class CityGalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['city_name_text']}),
        (None, {'fields': ['city_introduce_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('city_name_text', 'city_introduce_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['city_name_text']

admin.site.register(CityGallery, CityGalleryAdmin)
