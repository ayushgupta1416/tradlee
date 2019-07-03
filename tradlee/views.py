from django.http import HttpResponse
from django.template import loader
from .forms import sellForm, rentForm , rentFeedbackForm , sellFeedbackForm

def home(request):
    return HttpResponse('Home')
    pass


def sell(request):
    if request.method == 'POST':
        # save sell add
        # TODO
        return HttpResponse('form submitted!!<hr>page under construction')
    context = dict()
    context['form'] = sellForm()
    temp = loader.get_template('tradlee/sell.html')

    return HttpResponse(temp.render(context, request))


def rent(request):
    if request.method == 'POST':
        return HttpResponse('form submitted!!')
    context = dict()
    context['form'] = rentForm()
    temp = loader.get_template('tradlee/rent.html')
    return HttpResponse(temp.render(context, request))


def rentfeedback(request):
    if request.method == 'POST':
        return HttpResponse('feedback submitted!!')
    context = dict()
    context['form'] = rentFeedbackForm()
    temp = loader.get_template('tradlee/rentfeed.html')
    return HttpResponse(temp.render(context, request))


def sellfeedback(request):
    if request.method == 'POST':
        return HttpResponse('feedback submitted!!')
    context = dict()
    context['form'] = sellFeedbackForm()
    temp = loader.get_template('tradlee/sellfeed.html')
    return HttpResponse(temp.render(context, request))


def account(request, username):
    return HttpResponse('account ' + username)
    pass
