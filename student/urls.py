from django.urls import path
from student import views


urlpatterns = [
    path('get/', views.get_data, name='get-operation'),
]
