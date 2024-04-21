from django.contrib import admin
from .models import *

# @admin.register(JMenu)
# class PersonAdmin(admin.ModelAdmin):
#     pass

# class JmenuAdmin(admin.ModelAdmin):
#     list_display = ("id", "slug", "title", "ancestor", "descendant", "depth")
#     prepopulated_fields = {"slug" : ("title",)}
#
# class MainMenuAdmin(admin.ModelAdmin):
#     list_display = ("id", "slug", "title", "ancestor", "descendant", "depth")
#     prepopulated_fields = {"slug" : ("title",)}


class MenuAdmin(admin.ModelAdmin):
    list_display = ("slug", "title")
    prepopulated_fields = {"slug" : ("title",)}

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ("id", "slug", "title", "ancestor")
    prepopulated_fields = {"slug" : ("title",)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItems, MenuItemsAdmin)