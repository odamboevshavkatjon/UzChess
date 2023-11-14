from django.db import models
from ckeditor.fields import RichTextField
from helpers.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=255)

    image = models.ImageField(upload_to='news/')

    description = models.TextField()
    content = RichTextField()

    views = models.PositiveIntegerField(default=0)

    twitter_link = models.URLField()
    facebook_link = models.URLField()
    telegram_link = models.URLField()
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
