# products/urls.py
from django.urls import path
from .views import CatalogView, ProductCreateView, ProductUpdateView, ProductDeleteView, HomeView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
