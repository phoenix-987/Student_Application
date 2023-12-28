from django.urls import path
import student.views as views


urlpatterns = [
    path('delete/', views.delete_data, name='delete_operation')
]
