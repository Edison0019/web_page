"""web_personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from core.views import home
import core.views as views

from django.conf import settings #this option here is not default, it is just to showing images in developing stage

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('portafolio/', views.portafolio,name='portfolio'),
    path('',home,name='home'),
]

if settings.DEBUG: #this option here is not default, it is just to showing images in developing stage
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)