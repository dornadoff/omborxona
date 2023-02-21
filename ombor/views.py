from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, login, authenticate
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        user = authenticate(username=request.POST.get("login"),
                            password=request.POST.get("password"))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/ombor/bolim/")

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class BolimView(View):
    def get(self, request):
        return render(request, "bulimlar.html")

class MahsulotlarView(View):
    def get(self, request):
        # ombor1 = Ombor.objects.get(user=request.user)
        data = {"mahsulot":Mahsulot.objects.all()}
        return render(request, "products.html", data)

class ClientView(View):
    def get(self, request):
        data = {"client":Client.objects.all()}
        return render(request, "clients.html", data)
