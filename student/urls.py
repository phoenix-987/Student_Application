import student.views as views
from django.urls import path


urlpatterns = [
    path('post/', views.post_data, name='post-operation')
]
