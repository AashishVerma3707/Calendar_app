from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.Eventlist.as_view()),
]
