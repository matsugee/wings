from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('schedule/<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('schedule/new', views.schedule_new, name='schedule_new'),
    path('schedule/<int:pk>/edit/', views.schedule_edit, name='schedule_edit'),
]
