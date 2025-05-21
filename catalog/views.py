from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


#  Create your views here.

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        print(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
        return HttpResponse(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         print(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
#         return HttpResponse(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
#     return render(request, 'catalog/contacts.html')


# def home(request):
#     last_products = Product.objects.order_by('created_at')[:5]
#     products = Product.objects.all()
#     for product in last_products:
#         print(product)
#     context = {'products': products}
#     return render(request, 'catalog/home.html', context)
#
# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         print(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
#         return HttpResponse(f"Здравствуйте, {name}! Мы свяжемся с вами по номеру телефона {phone}")
#     return render(request, 'catalog/contacts.html')
#
# def product_detail(requets, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(requets, 'catalog/product_detail.html', context)
