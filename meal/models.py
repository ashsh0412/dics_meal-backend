from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField(null=True)
    allergic_notices = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MealSchedule(models.Model):
    meal_date = models.DateField()
    breakfast_menus = models.ManyToManyField(
        Menu, related_name="breakfast_schedules", blank=True
    )
    lunch_menus = models.ManyToManyField(
        Menu, related_name="lunch_schedules", blank=True
    )
    dinner_menus = models.ManyToManyField(
        Menu, related_name="dinner_schedules", blank=True
    )

    def __str__(self):
        return f"Meal Schedule for {self.meal_date}"
