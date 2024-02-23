from django.urls import path
from .views import CategoriaApiView, PlatoApiView

urlpatterns = [
    path('categorias/', CategoriaApiView.as_view()),
    path('platos/', PlatoApiView.as_view())
]