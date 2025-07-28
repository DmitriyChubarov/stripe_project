from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('item/<int:item_id>/', views.get_item, name='get_item'),
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
]
