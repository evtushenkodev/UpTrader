import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from menu.models import FoodMenu, FoodMenuItem


def load_data():
    # Удаляем существующее меню "main_menu"
    FoodMenu.objects.filter(name="main_menu").delete()

    # Создаем меню "main_menu"
    main_menu = FoodMenu.objects.create(name="main_menu", identifier="main_menu")

    # Создаем корневой объект "Dishes" в меню "main_menu"
    dishes_main = FoodMenuItem.objects.create(item_name="Dishes", item_slug="dishes", menu=main_menu)

    # Создаем объекты 2-го уровня в меню "main_menu"
    appetizers_main = FoodMenuItem.objects.create(item_name="Appetizers", item_slug="appetizers", menu=main_menu,
                                                  parent_item=dishes_main)
    main_courses_main = FoodMenuItem.objects.create(item_name="Main Courses", item_slug="main_courses",
                                                    menu=main_menu, parent_item=dishes_main)

    # Списки блюд
    appetizer_items = ["Salad", "Soup", "Bruschetta", "Calamari", "Spring Rolls"]
    main_course_items = ["Pasta", "Steak", "Sushi", "Pizza", "Burger"]

    # Создаем объекты 3-го уровня для закусок в меню "main_menu"
    for item in appetizer_items:
        FoodMenuItem.objects.create(item_name=item, item_slug=item.lower().replace(" ", "_"),
                                    parent_item=appetizers_main,
                                    menu=main_menu)

    # Создаем объекты 3-го уровня для основных блюд в меню "main_menu"
    for item in main_course_items:
        FoodMenuItem.objects.create(item_name=item, item_slug=item.lower().replace(" ", "_"),
                                    parent_item=main_courses_main,
                                    menu=main_menu)


if __name__ == "__main__":
    print("Loading data...")
    load_data()
    print("Food menu successfully loaded")
