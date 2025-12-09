from django.contrib import admin

from project.apps.page_to_pdf.models import Url, Page


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ["id", "name",]
    list_display_links = ["id", "name",]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "url_type",]
    list_display_links = ["id", "name",]
