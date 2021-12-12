from django.shortcuts import render

from django.http import HttpResponse

from .models import Category, Product, ItemImage


def categories_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories': categories,
    }
    return render(request, 'categories/categories_list.html', ctx)


def products_list(request, id):
    products = Product.objects.filter(categories=id)
    category = Category.objects.get(id=id)
    ctx = {
        'category': category,
        'products': products,
    }
    return render(request, 'categories/products_list.html', ctx)


def product_description(request, id):
    product = Product.objects.get(id=id)
    images = ItemImage.objects.filter(product=id)
    ctx = {
        'product': product,
        'images': images,
    }
    return render(request, 'categories/product_description.html', ctx)
