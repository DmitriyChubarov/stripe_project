from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import stripe

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, item_id):
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


def get_item(request, item_id):
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