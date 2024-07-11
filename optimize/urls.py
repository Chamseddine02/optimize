"""
URL configuration for optimize project.

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
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("store/<int:id>/", store_views.store, name="store"),
    path('store/edit/<int:store_id>/', store_views.edit_store, name='edit_store'),
    path('store/delete/<int:store_id>/', store_views.delete_store, name='delete_store'),
]
