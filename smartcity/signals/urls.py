from django.urls import path
from . import views

urlpatterns = [
    path('', views.feu_list, name='feu_list'),
    path('<int:pk>/', views.feu_detail, name='feu_detail'),
    path('add/', views.feu_create, name='feu_create'),
    path('<int:pk>/edit/', views.feu_update, name='feu_update'),
    path('<int:pk>/delete/', views.feu_delete, name='feu_delete'),
    path('<int:pk>/changer/', views.feu_changer_etat, name='feu_changer'),
]
