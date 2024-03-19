from django.urls import path

from habits.views import HabitCreateAPIView

app_name = 'habits'

urlpatterns = [
    path('create_habit/', HabitCreateAPIView.as_view(), name='habit_create')
]

