"""
URL configuration for user_service project.

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
from django.urls import path
from . import views
 
urlpatterns = [
    path('create/', views.create, name='create'),
    path('update/<str:pk>', views.update, name='update'),
    path('getdetails/pk=<str:pk>', views.get_details, name='get_details'),
    path('delete_user/<str:pk>', views.delete_user, name='delete_user'),
    path('get_all_user_list', views.get_all_user_list, name='get_all_user_list'),
    path('get_vehicle_by_id', views.get_vehicle_by_id, name='get_vehicle_by_id'),
]