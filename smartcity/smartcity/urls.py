from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',  auth_views.LoginView.as_view(template_name='auth/login.html'),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', include('dashboard.urls')),
    path('traffic/',   include('traffic.urls')),
    path('vehicles/',  include('vehicles.urls')),
    path('signals/',   include('signals.urls')),
    path('incidents/', include('incidents.urls')),
    path('parking/',   include('parking.urls')),
    path('', include('dashboard.urls')),
]
