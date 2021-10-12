from django.urls import path,include


from . import views

app_name="commentapp"

urlpatterns = [
    path('create/',views.Comment_Create_View.as_view(), name='create'),
    path('delete/<int:pk>',views.Comment_Delete_View.as_view(), name='delete'),
]
