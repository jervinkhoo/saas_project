# subscriptions/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import stripe

stripe.api_key = 'sk_test_51IAg8SGJnjtk2hcEYeRzSW8BRQEok4i3M4NKfY51dRnS88SjPS1mEh9LXwlm6HIePTFLAPsdgp897MQ4QkcoE1ci00hs6xo8J1'

def home(request):
    return render(request, 'home.html')  # Create a home.html template in your templates folder

@login_required
def choose_subscription(request):
    return render(request, 'subscriptions/choose_subscription.html')

@login_required
def make_payment(request):
    if request.method == 'POST':
        # Create a Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1OECwIGJnjtk2hcEoSLJsjPM',
                'quantity': 1,
            }],
            mode='subscription',
            success_url=request.build_absolute_uri('/subscriptions/confirm-payment/'),
            cancel_url=request.build_absolute_uri('/subscriptions/choose-subscription/'),
        )

        return redirect(checkout_session.url)

@login_required
def confirm_payment(request):
    return render(request, 'subscriptions/confirm_payment.html')
