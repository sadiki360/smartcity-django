from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicule_list, name='vehicule_list'),
    path('<int:pk>/', views.vehicule_detail, name='vehicule_detail'),
    path('add/', views.vehicule_create, name='vehicule_create'),
    path('<int:pk>/edit/', views.vehicule_update, name='vehicule_update'),
    path('<int:pk>/delete/', views.vehicule_delete, name='vehicule_delete'),
    path('missions/', views.mission_list, name='mission_list'),
    path('missions/add/', views.mission_create, name='mission_create'),
    path('missions/<int:pk>/edit/', views.mission_update, name='mission_update'),
]
