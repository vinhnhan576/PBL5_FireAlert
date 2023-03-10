from django.urls import path

from .views import FireAlertApiView

urlpatterns = [
    path('api', FireAlertApiView.as_view()),
]
