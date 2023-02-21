from django.contrib import admin
from django.urls import path, include
from ombor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LoginView.as_view(), name='login'),
    path("logout/", Logout.as_view(), name='logout'),
    path("ombor/", include("ombor.urls")),
    path("stats/", include("statistika.urls"))
]
