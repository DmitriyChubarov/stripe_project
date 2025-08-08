from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, item_id):
    '''Создание сессии на один товар'''
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return render(request, 'item.html', {'error': 'Товар не найден'})
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {'name': item.name},
            'unit_amount': item.price,
        },
        'quantity': 1,
    }],
    mode='payment',
    success_url='https://example.com/success',
    cancel_url='https://example.com/cancel',
    )
    return JsonResponse({'session_id': session.id})


def buy_order(request, order_id):
    '''Создание сессии на один заказ'''
    try:
        order = Order.objects.get(id=order_id) 
    except Order.DoesNotExist:
        return render(request, 'order.html', {'error': 'Заказ не найден'})

    line_items = [{
        'price_data': {
            'currency': 'usd',
            'product_data': {'name': item.name},
            'unit_amount': item.price,  
        },
        'quantity': 1,
    } for item in order.item.all()]  

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )

    return JsonResponse({'session_id': session.id})


def get_item(request, item_id):
    '''Вывод в HTML одного товара'''
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return render(request, 'item.html', {'error': 'Товар не найден'})
    context = {
        'item': item,
        'price_in_dollars': item.price / 100,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'item.html', context)

def get_items(request):
    '''Вывод в HTML всех товаров'''
    try:
        items = Item.objects.all()
    except Item.DoesNotExist:
        return render(request, 'items.html', {'error': 'Товары не загружаются или отсутствуют'})
    
    items_rub = []
    for item in items:
        items_rub.append({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price / 100
        })
    return render(request, 'items.html', {'items': items_rub})

def get_order(request, order_id):
    '''Вывод в HTML одного заказа'''
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return render(request, 'order.html', {'error': 'Ордер не найден'})
    
    order_rub = []
    for item in order.item.all():
        order_rub.append({
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price / 100
        })
    context = {
        'order': order,
        'order_rub': order_rub,
        'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'order.html', context)