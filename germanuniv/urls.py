"""
URL configuration for germanuniv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main_page, name='main_page'),
    path('add-school/', views.add_school, name='add_school'),
    path('delete-school/<int:school_id>/', views.delete_school, name='delete_school'),
    path('add-favorite/', views.add_favorite, name='add_favorite'),
    path('remove-favorite/<int:school_id>/', views.remove_favorite, name='remove_favorite'),
]