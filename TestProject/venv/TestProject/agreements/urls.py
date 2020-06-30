from django.urls import path
from . import views
from . import serializer

urlpatterns = [
    path('', views.index, name = '_index_'),
    path('calendar/',  views.CalendarList, name="calendar-list"),
]