from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('sell', views.sell),
    path('rent', views.rent),
    path('rentfeedback/<p_id>', views.rentfeedback),
    path('sellfeedback/<p_id>', views.sellfeedback),
    path('user/<username>/', views.user),
    path('accounts/signup/', views.signup),
    path('accounts/', include('django.contrib.auth.urls')),
]
