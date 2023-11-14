from django.db import models
from helpers.models import BaseModel
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=255)
    books_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    

class Book(BaseModel):
    class LanguageChoices(models.TextChoices):
        UZBEK = 'Uz'
        RUSSIAN = 'Ru'

    class LevelChoices(models.TextChoices):
        BEGINNER = 'Boshlang\'ich'
        PROFESSIONAL = 'Professional'
        AMATEUR = 'Havaskor'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    is_saved = models.ManyToManyField(User, related_name='saved_books')

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    preview = models.ImageField(upload_to='book-previews/')

    description = models.TextField()

    is_free = models.BooleanField(default=False)
    has_discount = models.BooleanField(default=False)

    original_price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)

    language = models.CharField(max_length=15, choices=LanguageChoices.choices)
    level = models.CharField(max_length=20, choices=LevelChoices.choices)

    published_date = models.DateField()

    pages_number = models.PositiveIntegerField(default=0)
    average_rating = models.PositiveIntegerField(default=0)
