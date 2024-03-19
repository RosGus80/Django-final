from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitListPaginator
from habits.serializers import HabitSerializer


# Create your views here.


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitListPaginator
