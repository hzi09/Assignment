from django.urls import path
from . import views


app_name = 'chatbot'
urlpatterns = [
    path('', views.py_tutor, name='py_tutor'),
]