from django.urls import path

from .views import *

urlpatterns = [
    path('notfication', FireAlertApiView.as_view()),
    path('fcmtoken', FireAlertExpoTokenApiView.as_view()),
    path('image', FireAlertImageApiView.as_view())
]
