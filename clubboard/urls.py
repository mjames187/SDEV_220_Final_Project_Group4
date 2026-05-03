from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='club_list'),
    path('club/<int:pk>/', views.club_detail, name='club_detail'),
    path('club/new/', views.club_new, name='club_new'),
    path('club/<int:club_pk>/post/new/', views.post_new, name='post_new'),
    path('post/<int:post_pk>/reply/new/', views.reply_new, name='reply_new'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]   