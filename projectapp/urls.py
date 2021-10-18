from django.urls import path

from . import views


app_name="projectapp"

urlpatterns = [
    path('create/',views.Create_Project_View.as_view(),name="create"),
    path('list/',views.Project_list.as_view(template_name='projectapp/list.html'),name="list"),
    path('detail/<int:pk>',views.Detail_Project_View.as_view(), name = 'detail'),
]
