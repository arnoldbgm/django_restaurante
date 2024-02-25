from django.urls import path
from .views import CategoriaApiView, PlatoApiView, PlatoDestroyApiView, ListarCategoriasApiView, RegistrarUsuariosApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('categorias/', CategoriaApiView.as_view()),
    path('categoria/<int:pk>', ListarCategoriasApiView.as_view()),
    path('platos/', PlatoApiView.as_view()),
    path('plato/<int:pk>', PlatoDestroyApiView.as_view()),
    path('registro/', RegistrarUsuariosApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
