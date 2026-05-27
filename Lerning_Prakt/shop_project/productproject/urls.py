from django.urls import path
from .views import *

app_name = 'productproject'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('plates/', PlateListView.as_view(), name='plate_list'),
    path('plates/<int:pk>/', PlateDetailView.as_view(), name='plate_detail'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('labels/', LabelListView.as_view(), name='label_list'),
    path('labels/<int:pk>/', LabelDetailView.as_view(), name='label_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('collections/', CollectionListView.as_view(), name='collection_list'),
    path('collections/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'),
    path('cart/', CartView.as_view(), name='cart'),
]
