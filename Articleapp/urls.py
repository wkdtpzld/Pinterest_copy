from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name='articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('create/', views.Article_Create_View.as_view(), name='create'),
    path('detail/<int:pk>', views.Article_Detail_View.as_view(), name='detail'),
    path('update/<int:pk>', views.Article_Update_View.as_view(), name='update'),
    path('delete/<int:pk>', views.Article_Delete_View.as_view(), name='delete'),
]