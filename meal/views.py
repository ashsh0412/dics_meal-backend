from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import MealSchedule
from .serializer import MealScheduleSerializer


class MealScheduleView(APIView):
    def get(self, request):
        # Calculate the start and end dates for the desired range
        today = datetime.now().date()
        start_date = today - timedelta(
            days=today.weekday()
        )  # Monday of the current week
        end_date = start_date + timedelta(days=6)  # Sunday of the current week

        meal_schedules = MealSchedule.objects.filter(
            meal_date__range=[start_date, end_date]
        )
        serializer = MealScheduleSerializer(meal_schedules, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealScheduleDetailView(APIView):
    def get_object(self, pk):
        try:
            meal_schedule = get_object_or_404(MealSchedule, pk=pk)
            return meal_schedule
        except MealSchedule.DoesNotExist:
            raise Http404("MealSchedule not found.")

    def get(self, request, pk):
        meal_schedule = self.get_object(pk)
        serializer = MealScheduleSerializer(meal_schedule)
        return Response(serializer.data)

    def put(self, request, pk):
        meal_schedule = self.get_object(pk)
        serializer = MealScheduleSerializer(meal_schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        meal_schedule = self.get_object(pk)
        meal_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
