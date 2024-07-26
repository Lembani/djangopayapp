from django.urls import path
from .views import test_moneyunify

urlpatterns = [
    path('', test_moneyunify, name='test-moneyunify'),
]
