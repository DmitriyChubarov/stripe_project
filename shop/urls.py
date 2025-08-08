from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('item/', views.get_items, name='get_items'),
    path('item/<int:item_id>/', views.get_item, name='get_item'),
    path('order/<int:order_id>/', views.get_order, name='get_order'),
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    path('buy_order/<int:order_id>/', views.buy_order, name='buy_order'),
]
