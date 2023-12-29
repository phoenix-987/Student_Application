import student.views as views
from django.urls import path
import student.views as views


urlpatterns = [
    path('delete/', views.delete_data, name='delete_operation'),
    path('post/', views.post_data, name='post-operation'),
    path('put/', views.put_data, name='post_operation'),
    path('get/', views.get_data, name='get-operation'),
]
