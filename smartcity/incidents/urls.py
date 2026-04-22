from django.urls import path
from . import views

urlpatterns = [
    path('', views.incident_list, name='incident_list'),
    path('<int:pk>/', views.incident_detail, name='incident_detail'),
    path('add/', views.incident_create, name='incident_create'),
    path('<int:pk>/edit/', views.incident_update, name='incident_update'),
    path('<int:pk>/delete/', views.incident_delete, name='incident_delete'),
    path('<int:pk>/resoudre/', views.incident_resoudre, name='incident_resoudre'),
]
