# -*- coding: utf-8 -*-
from django.contrib import admin
from favorites.models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',) 
    list_display = ('user', 'content_type', 'object_id', 'created')

admin.site.register(Favorite, FavoriteAdmin)