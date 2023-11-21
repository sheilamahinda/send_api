# alert_app/views.py

from rest_framework import generics
from .models import Alert
from .serializers import AlertSerializer

class AlertCreateView(generics.CreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
from django.shortcuts import render

# Create your views here.
