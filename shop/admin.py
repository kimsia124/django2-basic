# shop/admin.py

from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc','price', 'is_publish']
    list_display_links = ['pk', 'name', 'short_desc']
    list_filter = ['is_publish']
    search_fields = ['name']

    def short_desc(self,item):
        return item.desc[:20]
