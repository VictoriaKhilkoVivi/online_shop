from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название', max_length=256)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    content = models.TextField('Контент')
    categories = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    alt = models.CharField('Название', max_length=256)
    image = models.ImageField('Изображение', upload_to='images/')
    product = models.ForeignKey(Product, verbose_name='Картинка товара',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинка товаров'

    def __str__(self):
        return self.image.url
