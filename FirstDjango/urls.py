from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('home', views.home),
    path('item/<int:id>/', views.get_item,name='item-page'),
    path('items', views.get_items, name='items-list'),
]
