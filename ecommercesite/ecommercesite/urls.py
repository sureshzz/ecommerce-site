
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
