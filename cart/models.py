from django.db import models
from django.contrib.auth import get_user_model

from helpers.models import BaseModel
from library.models import Book


User = get_user_model()


class Item(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=0)


class Order(BaseModel):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'Active'
        DELIVERED = 'Delivered'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    email = models.EmailField()

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE
    )


class Coupon(BaseModel):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'Active'
        EXPIRED = 'Expired'

    title = models.CharField(max_length=8)

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE
    )

    discount_amount = models.PositiveIntegerField(default=0)
