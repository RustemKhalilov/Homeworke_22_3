# Generated by Django 5.0.6 on 2024-05-28 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Название категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Название категории",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Наименование продукта",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание продукта",
                        null=True,
                        verbose_name="Название продукта",
                    ),
                ),
                (
                    "foto",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото товара",
                        null=True,
                        upload_to="catalog/photo",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.CharField(
                        help_text="Укажите цену за единицу",
                        max_length=100,
                        verbose_name="Цена за единицу",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Укажите дату создания записи БД",
                        verbose_name="Дата записи в БД",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Укажите изменения записи в БД",
                        verbose_name="Дата записи в БД",
                    ),
                ),
                (
                    "manufactured_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Укажите дату производства",
                        verbose_name="Дата производства",
                    ),
                ),
                (
                    "my_category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите название категории",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="category_product",
                        to="catalog.category",
                        verbose_name="Категория продукта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
