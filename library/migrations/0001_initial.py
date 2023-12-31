# Generated by Django 4.2.7 on 2023-11-14 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("books_count", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("preview", models.ImageField(upload_to="book-previews/")),
                ("description", models.TextField()),
                ("is_free", models.BooleanField(default=False)),
                ("has_discount", models.BooleanField(default=False)),
                ("original_price", models.PositiveIntegerField(default=0)),
                ("discount_price", models.PositiveIntegerField(default=0)),
                ("language", models.CharField(choices=[("Uz", "Uzbek"), ("Ru", "Russian")], max_length=15)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Boshlang'ich", "Beginner"),
                            ("Professional", "Professional"),
                            ("Havaskor", "Amateur"),
                        ],
                        max_length=20,
                    ),
                ),
                ("published_date", models.DateField()),
                ("pages_number", models.PositiveIntegerField(default=0)),
                ("average_rating", models.PositiveIntegerField(default=0)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="library.category")),
                ("is_saved", models.ManyToManyField(related_name="saved_books", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
            },
        ),
    ]
