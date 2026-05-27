from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    pass

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass