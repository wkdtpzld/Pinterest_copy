from django.urls import path,include
from . import views

app_name='accountapp'

urlpatterns = [
    path('hello_world/',views.hello_world, name='hello_world'),
]
