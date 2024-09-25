from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
  list_display = ("url1", "url2", "joined_date",)

admin.site.register(Page, PageAdmin)
