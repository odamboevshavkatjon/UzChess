# Generated by Django 4.2.7 on 2023-11-13 19:05

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
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("title", models.CharField(max_length=255)),
                ("course_count", models.PositiveIntegerField(default=0)),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_createdby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modifiedby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("preview", models.ImageField(upload_to="course-preview")),
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
                ("average_rating", models.PositiveIntegerField(default=0)),
                ("module_count", models.PositiveIntegerField(default=0)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.category")),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_createdby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "is_completed",
                    models.ManyToManyField(related_name="completed_courses", to=settings.AUTH_USER_MODEL),
                ),
                (
                    "is_purchased",
                    models.ManyToManyField(related_name="purchased_courses", to=settings.AUTH_USER_MODEL),
                ),
                ("is_saved", models.ManyToManyField(related_name="saved_courses", to=settings.AUTH_USER_MODEL)),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modifiedby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("title", models.CharField(max_length=255)),
                ("lesson_count", models.PositiveIntegerField(default=0)),
                ("order", models.PositiveIntegerField(default=0)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_createdby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modifiedby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Module",
                "verbose_name_plural": "Module",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("title", models.CharField(max_length=255)),
                ("video_url", models.URLField()),
                ("description", models.TextField()),
                ("preview", models.ImageField(upload_to="lesson-preview")),
                ("is_accessable", models.BooleanField(default=False)),
                ("order", models.PositiveIntegerField(default=0)),
                ("bookmark", models.ManyToManyField(related_name="last_watched_lessons", to=settings.AUTH_USER_MODEL)),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_createdby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("is_watched", models.ManyToManyField(related_name="watched_lessons", to=settings.AUTH_USER_MODEL)),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modifiedby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.module")),
            ],
            options={
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lessons",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("rating", models.PositiveIntegerField(default=0)),
                ("content", models.TextField()),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="courses.course")),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_createdby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_modifiedby",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
    ]
