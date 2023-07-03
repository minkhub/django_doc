from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),  # '/' 에 해당되는 path
]