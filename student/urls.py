import student.views as views
from django.urls import path


urlpatterns = [

    path('post/', views.post_data, name='post-operation'),
    path('put/', views.put_data, name='post_operation'),
    path('get/', views.get_data, name='get-operation'),
]
