from django.urls import path,include
from . import views

app_name='profileapp'

urlpatterns = [
    path('create/', views.Profile_Create_View.as_view(), name='create'),
    path('update/<int:pk>', views.Profile_Update_View.as_view(), name='update'),
]
