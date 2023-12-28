import student.views as views
from django.urls import path


urlpatterns = [
    path('put/', views.put_data, name='post_operation')
]
