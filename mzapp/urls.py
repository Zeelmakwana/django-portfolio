# mzapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_page, name='home'),
    path('send-contact/', views.send_contact_email, name='send_contact'),
]