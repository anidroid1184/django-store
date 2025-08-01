from django.shortcuts import render


# Create your views here.
def cart(request):
    # request.session.set_expiry(300)  # set 5 minutos de sessión
    # key = request.session.session_key
    # print(f'Session Key: {key}')
    return render(request, 'carts/carts.html', {})
