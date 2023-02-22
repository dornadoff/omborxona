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
        ombor1 = Ombor.objects.get(user=request.user)
        qidirish = request.GET.get("qidirish")
        if qidirish is None:
            p1 = Mahsulot.objects.filter(ombor=ombor1)
        else:
            p1 = Mahsulot.objects.filter(ombor=ombor1, nom__contains=qidirish) or Mahsulot.objects.filter(ombor=ombor1, brend__contains=qidirish) or Mahsulot.objects.filter(ombor=ombor1, kelgan_sana__contains=qidirish)

        data = {"mahsulot":p1}
        return render(request, "products.html", data)

    def post(self, request):
        ombor1 = Ombor.objects.get(user=request.user)
        Mahsulot.objects.create(
            nom = request.POST.get("pr_name"),
            brend = request.POST.get("pr_brand"),
            narx = request.POST.get("pr_price"),
            kelgan_sana = request.POST.get("pr_data"),
            miqdor = request.POST.get("pr_amount"),
            olchov = request.POST.get("pr_olchov"),
            ombor = Ombor.objects.get(user=request.user)
        )
        return redirect("/ombor/mahsulot/")

class ClientView(View):
    def get(self, request):
        ombor1 = Ombor.objects.get(user=request.user)
        qidirish = request.GET.get("qidirish")

        if qidirish is None:
            c1 = Client.objects.filter(ombor=ombor1)
        else:
            c1 = Client.objects.filter(ombor=ombor1, ism__contains=qidirish) or Client.objects.filter(ombor=ombor1, nom__contains=qidirish) or Client.objects.filter(ombor=ombor1, manzil__contains=qidirish) or Client.objects.filter(ombor=ombor1, tel__contains=qidirish)
        data = {"client":c1}
        return render(request, "clients.html", data)

    def post(self, request):
        Client.objects.create(
            ism = request.POST.get("client_name"),
            nom = request.POST.get("client_shop"),
            manzil = request.POST.get("client_address"),
            tel = request.POST.get("client_phone"),
            qarz = request.POST.get("client_qarz"),
            ombor = Ombor.objects.get(user=request.user)
        )
        return redirect("/ombor/client/")

class DeleteView(View):
    def get(self, request, son):
        mahsulot = Mahsulot.objects.get(id=son)
        if Ombor.objects.get(user=request.user) == mahsulot.ombor:
            mahsulot.delete()
        return redirect("/ombor/mahsulot/")

class ClientDeleteView(View):
    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        if Ombor.objects.get(user=request.user) == client.ombor:
            client.delete()
        return redirect("/ombor/client/")

class MahsulotUpdateView(View):
    def get(self, request, pk):
        data = {
            "product":Mahsulot.objects.get(id=pk)
        }
        return render(request, "product_update.html", data)

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            narx=request.POST.get("price"),
            miqdor=request.POST.get("amount")
        )
        return redirect("/ombor/mahsulot/")

class ClientUpdateView(View):
    def get(self, request, pk):
        data = {
            "client":Client.objects.get(id=pk)
        }
        return render(request, "client_update.html", data)

    def post(self, request, pk):
        ombor1 = Ombor.objects.get(user=request.user)
        Client.objects.filter(id=pk, ombor=ombor1).update(
            ism=request.POST.get("client_name"),
            nom = request.POST.get("client_shop"),
            tel = request.POST.get("client_phone"),
            manzil = request.POST.get("client_address"),
            qarz = request.POST.get("client_qarz")
        )
        return redirect("/ombor/client/")

