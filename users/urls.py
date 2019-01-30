from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup_user, name='signup_user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile_photo', views.profile_photo, name='profile_photo'),
    path('create_event', views.create_event, name='create_event'),
    path('notifications', views.notifications, name='notifications'),
    path('join_requests', views.join_requests, name='join_requests'),
    path('lecture_request', views.lecture_request, name='lecture_request'),
    path('event_sign_up', views.event_sign_up, name='event_sign_up'),
    path('event_management', views.event_management, name='event_management'),
    path('event_update/<int:event_id>', views.event_update, name='event_update')
] 