from django.urls import path

from .views import FireAlertApiView, FireAlertExpoTokenApiView
from . import views

urlpatterns = [
    path('notfication', FireAlertApiView.as_view()),
    path('fcmtoken', FireAlertExpoTokenApiView.as_view()),
]
