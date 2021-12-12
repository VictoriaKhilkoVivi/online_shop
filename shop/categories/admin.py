from django.contrib import admin

from .models import Product, Category, ItemImage


class ImageAdmin(admin.ModelAdmin):
    list_display = ['alt']


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ItemImage, ImageAdmin)

