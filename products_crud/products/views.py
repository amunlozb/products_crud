# products/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product


class HomeView(TemplateView):
    template_name = 'products/home.html'


class LoginView(TemplateView):
    template_name = 'products/login.html'


class CatalogView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'brand', 'rating', 'price']


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'brand', 'rating', 'price']


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'  #
    success_url = reverse_lazy('catalog')
