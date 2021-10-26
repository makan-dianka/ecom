from django.contrib import admin
from django.urls import path
from . import views

# espace de nom
app_name = 'comapp'

urlpatterns = [
    path("", views.index, name='index'),
    path("details/<int:id>", views.details, name='details'),
    path("delete/<int:id>", views.on_delete, name='delete'),
#     path("pagne/<int:id>", views.pagne, name='pagne'),
 ]
