from django.shortcuts import render
from .serializer import EventSerializer
from rest_framework.generics import ListAPIView
from .models import Event
# Create your views here.

class Eventlist(ListAPIView):
    queryset=Event.objects.all()
    serializer_class = EventSerializer