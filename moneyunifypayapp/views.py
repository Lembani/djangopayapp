from django.shortcuts import render
from moneyunify import MoneyUnifyClient, ApiError, TimeoutError

def test_moneyunify(request):
    response = None

    if request.method == 'POST':
        muid = '' # Replace with your own MUID from the MoneyUnify dashboard
        client = MoneyUnifyClient(muid)

        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        try:
            response = client.request_payment(phone_number, amount)
        except ApiError as e:
            response = {'error': str(e)}
        except TimeoutError as e:
            response = {'error': str(e)}

    return render(request, 'moneyunifypayapp/payment_form.html', {'response': response})
