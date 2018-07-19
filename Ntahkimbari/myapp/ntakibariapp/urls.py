from django.urls import path 
from . import views


app_name = 'ntakimbari'

urlpatterns = [
    path('',views.index, name='index'), 
    path('register/', views.register, name='register'),
    path('login/', views._login, name='_login'), 
    path('organigram/', views.organigram, name='organigram'), 
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('community_work/', views.community_work, name='community_work'), 
    path('gallery/', views.gallery, name='gallery'), 
    path('<int:post_id>/fun/', views.post, name='post'), 
    path('project/', views.project, name='project'), 
    path('success-projects/', views.success, name='success'), 
    path('<int:event_id>/event/', views.event, name='event' ), 
    path('members/', views.members, name='members'),
    path('<int:member_id>/upload/', views.uploadProfile, name='upload')
]