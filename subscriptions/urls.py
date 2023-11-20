# subscriptions/urls.py
from django.urls import path
from .views import choose_subscription, make_payment, confirm_payment, home

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root path
    path('choose-subscription/', choose_subscription, name='choose_subscription'),
    path('make-payment/', make_payment, name='make_payment'),
    path('confirm-payment/', confirm_payment, name='confirm_payment'),
]
