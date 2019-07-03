from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('sell', views.sell),
    path('rent', views.rent),
    path('rentfeedback', views.rentfeedback),
    path('sellfeedback', views.sellfeedback),
    path('account/<username>/', views.account)
]
