from rest_framework import serializers
from .models import MealSchedule


class MealScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealSchedule
        fields = "__all__"
        depth = 1
