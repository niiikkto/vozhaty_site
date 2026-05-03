from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Role, CustomUser, Material, GalleryImage

admin.site.register(Role)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
    )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("title", "material_type", "uploaded_at")
    list_filter = ("material_type", "uploaded_at")
    search_fields = ("title", "description")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")
    list_filter = ("uploaded_at",)
