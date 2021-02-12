from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('about/', views.about, name= "about"),
    path('create/', views.create, name= "create"),
    path('delete/<Todos_id>', views.delete, name= "delete"),
    path('yesfinish/<Todos_id>', views.yesfinish, name= "yesfinish"),
    path('nofinish/<Todos_id>', views.nofinish, name= "nofinish"),
    path('update/<Todos_id>', views.update, name= "update"),
]