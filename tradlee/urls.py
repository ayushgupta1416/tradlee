from django.contrib import admin
from django.urls import path
from apps import *;
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('ad_post', views.ad_post),
    path('account/<username>/', views.account)
]
