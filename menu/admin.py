from django.contrib import admin

from menu.models import FoodMenu, FoodMenuItem


@admin.register(FoodMenuItem)
class FoodMenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for FoodMenuItem model.
    """
    list_display = ('pk', 'item_name', 'parent_item')
    list_filter = ('menu',)
    search_fields = ('item_name', 'item_slug')
    ordering = ('pk',)

    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent_item'), 'item_name', 'item_slug')
            }),
    )


@admin.register(FoodMenu)  # Изменили регистрацию модели
class FoodMenuAdmin(admin.ModelAdmin):
    """
    Admin configuration for FoodMenu model.
    """
    list_display = ('name', 'identifier')
    search_fields = ('name', 'identifier')
