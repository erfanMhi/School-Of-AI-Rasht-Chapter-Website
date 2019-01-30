from django.urls import path

from . import views

urlpatterns = [
    path('<int:event_id>/event', views.event_details, name='event_details'),
    path('', views.events_page, name='events'),
    path('page/<int:page>', views.events_page, name='events_page'),
    path('page/<int:page>/category/<int:category_id>', views.events_page, name='events_page')
]