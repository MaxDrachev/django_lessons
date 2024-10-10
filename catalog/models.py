from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    photo_prod = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(
        null=False,
        verbose_name="цена за покупку",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата создания",
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="дата последнего изменения(записи в БД)",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} {self.price}"
