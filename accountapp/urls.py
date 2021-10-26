from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name='accountapp'

urlpatterns = [
    
    path('create/', views.Account_Create_View.as_view(), name='create'),
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('detail/<int:pk>/', views.Account_Detail_View.as_view(), name='detail'),
    path('update/<int:pk>/', views.Account_Update_View.as_view(), name='update'),
    path('delete/<int:pk>/', views.Account_Delete_View.as_view(), name='delete'),

]
