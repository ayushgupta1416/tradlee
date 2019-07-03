from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('sell', views.sell),
    path('rent', views.rent),
    path('account/<username>/', views.account)
]
