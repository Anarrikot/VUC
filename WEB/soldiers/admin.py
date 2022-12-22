from django.contrib import admin
from soldiers.models import Solder, Title


class SolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'number', 'birth_date')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name')
    prepopulated_fields = {"slug": ("last_name",)}

class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


# Register your models here.
admin.site.register(Solder, SolderAdmin)
admin.site.register(Title, TitleAdmin)