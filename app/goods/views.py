from turtle import title
from django.shortcuts import render
from .models import Categories, Products


def category(request):
    pass


def catalog(request):
    products = Products.objects.all()
    context = {
        "title": "HOME - Каталог",
        "goods": products,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
