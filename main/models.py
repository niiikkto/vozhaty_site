# main/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название роли")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        ordering = ["name"]


class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Роль"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    groups = models.ManyToManyField(
        "auth.Group", related_name="customuser_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="customuser_set", blank=True
    )

    def __str__(self):
        return self.get_full_name() or self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название материала")
    description = models.TextField(verbose_name="Описание")

    material_type = models.CharField(
        max_length=50,
        choices=[
            ("theory", "Теория и методички"),
            ("games", "Игры"),
            ("scenarios", "Сценарии"),
            ("other", "Другое"),
        ],
        default="other",
        verbose_name="Тип материала",
    )

    file = models.FileField(upload_to="materials/", verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ["-uploaded_at"]


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", blank=True)
    image = models.ImageField(upload_to="gallery/", verbose_name="Фото")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Фото {self.id}"

    class Meta:
        verbose_name = "Фото галереи"
        verbose_name_plural = "Фото галереи"
        ordering = ["-uploaded_at"]
