import student.views as views
from django.urls import path
from student import views


urlpatterns = [
    path('put/', views.put_data, name='post_operation'),
    path('get/', views.get_data, name='get-operation'),
]
