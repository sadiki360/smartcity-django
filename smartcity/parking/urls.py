from django.urls import path
from . import views

urlpatterns = [
    path('', views.parking_list, name='parking_list'),
    path('<int:pk>/', views.parking_detail, name='parking_detail'),
    path('add/', views.parking_create, name='parking_create'),
    path('<int:pk>/edit/', views.parking_update, name='parking_update'),
    path('<int:pk>/delete/', views.parking_delete, name='parking_delete'),
    path('bornes/add/', views.borne_create, name='borne_create'),
]
