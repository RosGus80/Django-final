from django.urls import path

from habits.views import HabitCreateAPIView, HabitListAPIView

app_name = 'habits'

urlpatterns = [
    path('habit_create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit_list', HabitListAPIView.as_view(), name='habit_list'),
]

