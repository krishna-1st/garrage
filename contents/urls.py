"""
URL configuration for garrage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contact', views.contacts, name='contact'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('login', views.login_p, name='login'),
    path('logout', views.logout_p, name='logout'),
    path('landing', views.landing, name='landing'),
    path('viewf', views.viewform, name='viewf'),
    path('pratice', views.pratice, name='pratice'),
    path('add', views.add_d, name='add'),
    # path('edit', views.edit, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('update/<str:id>', views.update, name='update'),
    

    
]
