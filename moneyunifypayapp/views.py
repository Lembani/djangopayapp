from django.shortcuts import render

from django.http import JsonResponse
from moneyunify import MoneyUnifyClient, ApiError, TimeoutError

def test_moneyunify(request):
    client = MoneyUnifyClient(muid='') # Replace with your own MUID from the MoneyUnify dashboard
    phone_number = '0765655244'
    amount = 1

    try:
        response = client.request_payment(phone_number, amount)
        return JsonResponse(response)
    except ApiError as e:
        return JsonResponse({'error': str(e)}, status=500)
    except TimeoutError as e:
        return JsonResponse({'error': str(e)}, status=500)

