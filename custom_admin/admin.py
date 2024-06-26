from django.contrib import admin
from .models import Site

class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'page_title')  # Kolom yang ditampilkan di list view
    search_fields = ('site_name', 'page_title')  # Kolom yang dapat dicari

admin.site.register(Site, SiteAdmin)
