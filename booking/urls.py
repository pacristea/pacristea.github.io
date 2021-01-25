from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_index, name="booking_index"),
    path("<int:pk>/", views.booking_service_detail, name="booking_service_detail"),
]