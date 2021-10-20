from django.urls import path
from . import views

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/',views.Subscription_View.as_view(), name='subscribe'),
]
