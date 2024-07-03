from django.db import models
from django.conf import settings
from store.models import Shirt, ShirtSize
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Cart(models.Model):
    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE, related_name="cart")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart",
        default=None,
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.shirt.name}-{self.shirt.id}"


class Address(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses",
        default=None,
    )

    def __str__(self) -> str:
        return f"{self.first_name}-{self.user.id}"


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
        default=None,
    )
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="orders"
    )
    ordered = models.BooleanField(default=False)  # True if order is placed

    def __str__(self) -> str:
        return f"{self.id}-{self.user.id}"


# a order can have multiple shirts
# This is a many to many relationship
class OrderShirt(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_shirts"
    )
    shirt = models.ForeignKey(
        Shirt, on_delete=models.CASCADE, related_name="order_shirts"
    )
    shirt_size = models.ForeignKey(
        ShirtSize, on_delete=models.CASCADE, related_name="order_shirts"
    )
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )  # quantity of the shirt in the order max 10
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.shirt.name}-{self.order.id}"