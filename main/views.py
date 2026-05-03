from django.shortcuts import render, redirect
from .models import Material, GalleryImage


def entry(request):
    return redirect("index")


def index(request):
    """Главная страница"""
    materials = Material.objects.all().order_by("-uploaded_at")[:12]
    gallery_images = GalleryImage.objects.all().order_by("-uploaded_at")[:8]

    return render(
        request,
        "index.html",
        {
            "materials": materials,
            "gallery_images": gallery_images,
        },
    )
