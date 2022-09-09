from django.urls import path, include
from AppTwo import views


urlpatterns = [
    path('', views.index, name=' '),
    path('users', views.users, name='user list')

]