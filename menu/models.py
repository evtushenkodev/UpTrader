from django.db import models


class FoodMenu(models.Model):
    """
    Represents a food menu, which can contain multiple food items.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name='Menu name')
    identifier = models.SlugField(max_length=255, verbose_name="Menu identifier")

    class Meta:
        verbose_name = 'Food Menu'
        verbose_name_plural = 'Food Menus'

    def __str__(self) -> str:
        return self.name


class FoodMenuItem(models.Model):
    """
    Represents a food menu item that can be nested in a hierarchical structure.
    """
    item_name = models.CharField(max_length=255, verbose_name='Item name')
    item_slug = models.SlugField(max_length=255, verbose_name="Item slug")

    menu = models.ForeignKey(
        FoodMenu, blank=True, related_name='items', on_delete=models.CASCADE
    )
    parent_item = models.ForeignKey(
        'self', blank=True, null=True, related_name='sub_items', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Food Menu Item'
        verbose_name_plural = 'Food Menu Items'

    def __str__(self) -> str:
        return self.item_name
