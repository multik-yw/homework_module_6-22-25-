from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        print(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
        return HttpResponse(
            f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}"
        )
    return render(request, "catalog/contacts.html")
