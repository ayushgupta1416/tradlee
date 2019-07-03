from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')
    pass


def ad_post(request):
    return HttpResponse('ad_post')
    pass


def account(request, username):
    return HttpResponse('account ' + username)
    pass
