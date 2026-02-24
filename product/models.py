from django.db import models
from decimal import Decimal
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField("Название", max_length=255)
    icon = models.ImageField("Иконка", upload_to='subcategory_icons/', blank=True, null=True)
    description = RichTextField("Описание")
    

    def __str__(self):
        return self.name


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField("Название", max_length=255)
    description = RichTextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Изображение", upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name
