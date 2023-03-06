from django.contrib import admin
from .models import Menu, MenuElements
# Register your models here.


class MenuElementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('parent',)
    search_fields = ('name',)


admin.site.register(MenuElements, MenuElementsAdmin)
admin.site.register(Menu)
