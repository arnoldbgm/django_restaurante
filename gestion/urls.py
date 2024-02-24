from django.urls import path
from .views import CategoriaApiView, PlatoApiView, PlatoDestroyApiView, ListarCategoriasApiView

urlpatterns = [
    path('categorias/', CategoriaApiView.as_view()),
    path('categoria/<int:pk>', ListarCategoriasApiView.as_view()),
    path('platos/', PlatoApiView.as_view()),
    path('plato/<int:pk>', PlatoDestroyApiView.as_view()),
]
