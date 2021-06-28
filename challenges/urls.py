from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("<int:monthNumber>", views.monthly_challenge_by_number),
    path("<str:monthName>", views.monthly_challenge, name="month-challenge")
]
