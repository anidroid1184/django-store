from django.urls import path, include
from . import views

urlpatterns = [
    path('user/registro/', views.registro, name='registro'),
    path('user/login/', views.login, name='login'),
    path('user/logout/', views.logout, name='logout'),
    # autenticación con facebook
    path('social-auth/', include('social_django.urls', namespace="social")),
]
