from django import forms
from .models import Plate, Artist, Label

class PlateForm(forms.ModelForm):
    class Meta:
        model = Plate
        fields = ['name', 'description', 'price', 'year', 'photo',
                    'category', 'artist', 'label', 'genre', 
                    'vinyl_format', 'condition', 'collection']
        
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'description', 'country', 'photo']


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'description', 'country', 'logo']