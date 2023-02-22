from django.urls import path
from .views import *

urlpatterns = [
    path("bolim/", BolimView.as_view()),
    path("mahsulot/", MahsulotlarView.as_view()),
    path("client/", ClientView.as_view()),
    path("mahsulot/delete/<int:son>/", DeleteView.as_view()),
    path("client/delete/<int:pk>/", ClientDeleteView.as_view()),
    path("mahsulot/update/<int:pk>/", MahsulotUpdateView.as_view()),
    path("client/update/<int:pk>/", ClientUpdateView.as_view())
]