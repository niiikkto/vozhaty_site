# main/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Логин
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    
    # Выход — исправляем на POST
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    
    # Регистрация
    path('register/', views.register, name='register'),
]