from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=256)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)
    content = models.TextField('Контент')
    # image = models.ImageField('Изображение', upload_to='categories/', null=True, blank=True)
    # date_created = models.DateField('Дата публикации')
    categories = models.ManyToManyField('Category', verbose_name='Категории')
    images = models.ImageField(null=True, blank=True, upload_to='images/',
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


# class ItemImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     author = models.CharField(max_length=256)
#     text = models.TextField()
#     date = models.DateField()
#
#     class Meta:
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'
#
#     def __str__(self):
#         return f'{self.author} - {self.date}'


class Category(models.Model):
    name = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
