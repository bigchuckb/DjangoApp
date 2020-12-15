from django.forms import ModelForm
from collection.models import Books

class ThingForm(ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'description',)