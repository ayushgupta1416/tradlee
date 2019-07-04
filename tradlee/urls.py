from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('sell', views.sell),
    path('rent', views.rent),
    path('rentfeedback/<p_id>', views.rentfeedback),
    path('sellfeedback/<p_id>', views.sellfeedback),
    path('account/<username>/', views.account)
]
