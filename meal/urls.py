from django.urls import path
from .views import MealScheduleView, MealScheduleDetailView

urlpatterns = [
    path("", MealScheduleView.as_view(), name="meal_schedule_list"),
    path(
        "<int:pk>/",
        MealScheduleDetailView.as_view(),
        name="meal_schedule_detail",
    ),
]
