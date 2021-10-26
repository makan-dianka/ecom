from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("details/<int:id>", views.details, name='details'),
    path("pagne/<int:id>", views.pagne, name='pagne'),
]
