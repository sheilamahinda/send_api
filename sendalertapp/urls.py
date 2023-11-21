# alert_app/urls.py

from django.urls import path
from .views import AlertCreateView

urlpatterns = [
    path('send-alert/', AlertCreateView.as_view(), name='send-alert'),
]
