from django.urls import path,include
from . import views

app_name='profileapp'

urlpatterns = [
    path('create/', views.Profile_Create_View.as_view(), name='create'),
]
