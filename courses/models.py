from django.db import models
from django.contrib.auth import get_user_model
from helpers.models import BaseModel


User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=255)
    course_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Course(BaseModel):
    class LanguageChoices(models.TextChoices):
        UZBEK = 'Uz'
        RUSSIAN = 'Ru'

    class LevelChoices(models.TextChoices):
        BEGINNER = 'Boshlang\'ich'
        PROFESSIONAL = 'Professional'
        AMATEUR = 'Havaskor'
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    is_saved = models.ManyToManyField(User, related_name='saved_courses')
    is_purchased = models.ManyToManyField(User, related_name='purchased_courses')
    is_completed = models.ManyToManyField(User, related_name='completed_courses')

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    preview = models.ImageField(upload_to='course-previews/')

    is_free = models.BooleanField(default=False)
    has_discount = models.BooleanField(default=False)

    original_price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)

    language = models.CharField(max_length=15, choices=LanguageChoices.choices)
    level = models.CharField(max_length=20, choices=LevelChoices.choices)

    average_rating = models.PositiveIntegerField(default=0)
    module_count = models.PositiveIntegerField(default=0)

    @property
    def discount_percentage(self):
        return (100 - ((self.discount_price / self.original_price) * 100))


class Module(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    lesson_count = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)


class Lesson(BaseModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    is_watched = models.ManyToManyField(User, related_name='watched_lessons')
    bookmark = models.ManyToManyField(User, related_name='last_watched_lessons')

    title = models.CharField(max_length=255)

    video_url = models.URLField()
    description = models.TextField()
    preview = models.ImageField(upload_to='lesson-previews/')

    is_accessable = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)
    

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    rating = models.PositiveIntegerField(default=0)
    content = models.TextField()
