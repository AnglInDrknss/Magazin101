from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField("Заголовок", max_length=255, blank=True, default="")
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField("Название", max_length=255)
    icon = models.ImageField("Иконка", upload_to='subcategory_icons/', blank=True, null=True)
    description = RichTextField("Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField("Название", max_length=255)
    description = RichTextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ForeignKey('ProductImage', on_delete=models.SET_NULL, blank=True, null=True, related_name='product_main_image')
    sort_order = models.IntegerField("Порядок сортировки", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("Изображение", upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"
        ordering = ['-created_at']

    def __str__(self):
        return f"Image for {self.product.name}"

class SocialMedia(models.Model):
    name = models.CharField("Название сети", max_length=255)
    url = models.URLField("URL", max_length=500)
    icon = models.ImageField("Иконка", upload_to='social_media_icons/', blank=True, null=True)

    class Meta:
        verbose_name = "Социальная сеть"
        verbose_name_plural = "Социальные сети"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} for {self.product.name}"

