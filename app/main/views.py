from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "HOME - О нас",
        "content": "О нас",
        "text_on_page": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
    }
    return render(request, "main/about.html", context)


def shipping(request):
    context = {
        "title": "HOME - Доставка",
        "content": "Доставка",
        "text_on_page": [
            {
                "title": "Железнодорожный",
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                "price": f"стоимость: {15.60}$",
            },
            {
                "title": "Морской",
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                "price": f"стоимость: {15.60}$",
            },
            {
                "title": "Авиа",
                "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",
                "price": f"стоимость: {15.60}$",
            },
        ],
    }
    return render(request, "main/shipping.html", context)
