from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('posts/', views.posts, name='posts'),
    path('tags/', views.tags, name='tags'),
    path('users/', views.users, name='users'),
]
