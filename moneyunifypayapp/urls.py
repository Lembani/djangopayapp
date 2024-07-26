from django.urls import path
from .views import test_moneyunify

urlpatterns = [
    path('test-moneyunify/', test_moneyunify, name='test-moneyunify'),
]
