from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('posts/', views.posts, name='posts'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<str:name_post>/', views.post, name='post'),
    path('posts/<str:name_post>/comment/', views.create_comment, name='post'),
    path('tags/', views.tags, name='tags'),
    path('tags/create/', views.create_tag, name='create_tag'),
    path('users/', views.users, name='users'),
    path('profile/<str:username>/', views.profile, name='users'),
]
