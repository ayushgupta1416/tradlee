from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SellForm, RentForm, RentFeedbackForm, SellFeedbackForm, SignupForm
from .models import *

def home(request):
    return render(request,'home.html')
    pass


def sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SellForm()
    context = dict()
    context['form'] = form
    temp = loader.get_template('tradlee/sell.html')

    return HttpResponse(temp.render(context, request))


def rent(request):
    if request.method == 'POST':
        form = RentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RentForm()
    context = dict()
    context['form'] = form
    temp = loader.get_template('tradlee/rent.html')
    return HttpResponse(temp.render(context, request))


def rentfeedback(request, p_id):
    if request.method == 'POST':
        return HttpResponse('feedback submitted for product id' + p_id)
    context = dict()
    context['form'] = RentFeedbackForm()
    temp = loader.get_template('tradlee/rentFeed.html')
    return HttpResponse(temp.render(context, request))


def sellfeedback(request, p_id):
    if request.method == 'POST':
        return HttpResponse('feedback submitted for product id' + p_id)
    context = dict()
    context['form'] = SellFeedbackForm()
    temp = loader.get_template('tradlee/sellFeed.html')
    return HttpResponse(temp.render(context, request))


def user(request, username):
    return HttpResponse('account ' + username)
    pass

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})