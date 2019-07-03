from django.http import HttpResponse
from django.template import loader
from .forms import sellForm, rentForm

def home(request):
    return HttpResponse('Home')
    pass


def sell(request):
    if request.method == 'POST':
        return HttpResponse('form submitted!!')
    context = dict()
    context['form'] = sellForm()
    temp = loader.get_template('tradlee/sell.html')

    return HttpResponse(temp.render(context, request))


def account(request, username):
    return HttpResponse('account ' + username)
    pass
