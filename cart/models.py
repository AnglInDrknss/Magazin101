from django.db import models


# Create your models here.

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    products = models.ManyToManyField("Product", through="CartItem")

    def get_total_price(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.product.price * item.quantity
        return total

    def add_product(self, product_id, quantity):
        item, created = CartItem.objects.get_or_create(
            cart=self,
            product_id=product_id
        )

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity

        item.save()

    def remove_product(self, product_id):
        CartItem.objects.filter(cart=self, product_id=product_id).delete()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)