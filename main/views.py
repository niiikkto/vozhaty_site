# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Material, GalleryImage


def index(request):
    """Главная страница"""
    materials = Material.objects.all().order_by('-uploaded_at')[:12]
    gallery_images = GalleryImage.objects.all().order_by('-uploaded_at')[:8]

    return render(request, 'index.html', {
        'materials': materials,
        'gallery_images': gallery_images,
    })


def register(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно! Теперь вы можете войти.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})