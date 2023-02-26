from django.shortcuts import render, redirect
from django.views import View
from .models import *

class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            qidirish = request.GET.get("qidirish")
            if qidirish is None:
                st = Statistika.objects.filter(ombor__user=request.user)
            else:
                st = Statistika.objects.filter(ombor__user=request.user, mahsulot__nom__contains=qidirish)


            data = {
                "statistika": st,
                "mahsulot": Mahsulot.objects.filter(ombor__user=request.user),
                "client": Client.objects.filter(ombor__user=request.user)
            }
            return render(request, "stats.html", data)
        return redirect("/")

    def post(self, request):
        Statistika.objects.create(
            mahsulot = Mahsulot.objects.get(id=request.POST.get("product")),
            client = Client.objects.get(id=request.POST.get("client")),
            miqdor = request.POST.get("miqdor"),
            sana = request.POST.get("sana"),
            umumiy_summa = request.POST.get("summa"),
            tolandi = request.POST.get("tolandi"),
            nasiya = request.POST.get("nasiya"),
            ombor = Ombor.objects.get(user=request.user)
        )
        m = Mahsulot.objects.get(id=request.POST.get("product"))
        m.miqdor = int(m.miqdor) - int(request.POST.get("miqdor"))
        m.save()
        cl = Client.objects.get(id=request.POST.get("cl"))
        cl.qarz = int(cl.qarz) + int(request.POST.get("nasiya"))
        return redirect("/stats/")
class StatistikaDeleteView(View):
    def get(self, request, pk):
        Statistika.objects.get(id=pk, ombor__user=request.user).delete()
        # mahsulot = Statistika.objects.get(id=pk)
        # if Ombor.objects.get(user=request.user) == mahsulot.ombor:
        #     mahsulot.delete()
        return redirect("/stats/")



