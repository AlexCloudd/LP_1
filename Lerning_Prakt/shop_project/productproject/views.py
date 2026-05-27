from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from .models import (
    Plate, Artist, Label, Category, 
    Collection, Genre, VinylFormat, Condition
)

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class PlateListView(ListView):
    model = Plate
    template_name = 'plates/plate_list.html'
    context_object_name = 'plates'

class PlateDetailView(DetailView):
    model = Plate
    template_name = 'plates/plate_detail.html'
    context_object_name = 'plate'

class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artist_list.html'
    context_object_name = 'artists'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/artist_detail.html'
    context_object_name = 'artist'

class LabelListView(ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'

class LabelDetailView(DetailView):
    model = Label
    template_name = 'labels/label_detail.html'
    context_object_name = 'label'

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'

class CollectionListView(ListView):
    model = Collection
    template_name = 'collections/collection_list.html'
    context_object_name = 'collections'

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collections/collection_detail.html'
    context_object_name = 'collection'