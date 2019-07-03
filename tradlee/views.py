from django.http import HttpResponse
from django.template import loader
from .forms import *

def home(request):
    return HttpResponse('Home')
    pass


def sell(request):
    if request.method == 'POST':
        return HttpResponse('form submitted!!')

    return HttpResponse('ad_post')


def account(request, username):
    return HttpResponse('account ' + username)
    pass
