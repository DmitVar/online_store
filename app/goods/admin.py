from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Класс регистрации таблицы Категории в панели администратора"""

    # автоматическое добавление значения slug по имени категории
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """Класс регистрации таблицы Продукты в панели администратора"""

    # автоматическое добавление значения slug по имени продукта
    prepopulated_fields = {"slug": ("name",)}
