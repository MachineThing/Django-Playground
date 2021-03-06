"""playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from playground import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('python_compiler/', views.python_compiler, name="python_compiler"),
    path('ajax_test/', views.ajax_test, name="ajax_test"),
    path('ajax/retxt/', views.ajax_text, name="__retxt"),
    #path('admin/', admin.site.urls),
]
