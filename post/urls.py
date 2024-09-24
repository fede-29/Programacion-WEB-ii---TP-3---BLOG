from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('ver/', views.ver_publicaciones, name='ver_publicaciones'),
    path('eliminar/<int:publicacion_id>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('publicacion/<int:publicacion_id>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('registro/', views.registro_usuario, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]