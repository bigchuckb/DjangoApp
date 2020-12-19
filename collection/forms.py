from django.forms import ModelForm
from collection.models import Books, Rating, Shtetl

class ThingForm(ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'description', 'author', 'owner')

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('rating','user','book')

class ShtetlForm(ModelForm):
    class Meta:
        model = Shtetl
        fields = ('winner',)
