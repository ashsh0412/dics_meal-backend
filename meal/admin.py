from django.contrib import admin
from .models import Menu, MealSchedule


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "calories", "allergic_notices"]


@admin.register(MealSchedule)
class MealScheduleAdmin(admin.ModelAdmin):
    list_display = ["meal_date", "get_meal_type", "get_menus"]

    def get_meal_type(self, obj):
        meal_type = []
        if obj.breakfast_menus.exists():
            meal_type.append("Breakfast")
        if obj.lunch_menus.exists():
            meal_type.append("Lunch")
        if obj.dinner_menus.exists():
            meal_type.append("Dinner")
        return ", ".join(meal_type)

    get_meal_type.short_description = "Meal Type"

    def get_menus(self, obj):
        menus = []
        if obj.breakfast_menus.exists():
            breakfast_menus = ", ".join(
                [menu.name for menu in obj.breakfast_menus.all()]
            )
            menus.append(f"Breakfast: {breakfast_menus}")
        if obj.lunch_menus.exists():
            lunch_menus = ", ".join([menu.name for menu in obj.lunch_menus.all()])
            menus.append(f"Lunch: {lunch_menus}")
        if obj.dinner_menus.exists():
            dinner_menus = ", ".join([menu.name for menu in obj.dinner_menus.all()])
            menus.append(f"Dinner: {dinner_menus}")
        return ", ".join(menus)

    get_menus.short_description = "Menus"
