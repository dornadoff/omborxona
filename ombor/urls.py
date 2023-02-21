from django.urls import path
from .views import *

urlpatterns = [
    path("bolim/", BolimView.as_view()),
    path("mahsulot/", MahsulotlarView.as_view()),
    path("client/", ClientView.as_view())
]