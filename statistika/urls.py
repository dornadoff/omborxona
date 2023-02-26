from django.urls import path
from .views import *

urlpatterns = [
    path("", StatistikaView.as_view()),
    path("delete/<int:pk>/", StatistikaDeleteView.as_view())
]