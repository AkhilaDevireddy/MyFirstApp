"""MyFirstApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from biryani import views as biryani_views

urlpatterns = [
    path('', biryani_views.get_biryani_details, name='List of Biryani Details'), 
    path('get_biryani_details/', biryani_views.get_biryani_details_by_name, name='Get Biryani Details By Biryani Name'), 
    path('add_biryani_details/', biryani_views.add_biryani_details, name='Add Biryani Details'), 
    path('update/<biryani_name>/', biryani_views.update_biryani_details, name='Update Biryani By Name'),                        # Dynamic URL
    path('delete_biryanis/', biryani_views.delete_biryanis, name='Delete Biryanis'), 
    path('delete_biryani_by_name/<biryani_name>/', biryani_views.delete_biryani_by_name, name='Delete Biryani By Name'),        # Dynamic URL
]
