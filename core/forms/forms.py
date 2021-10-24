from django import forms
from core.models import Animal


# DataFlair
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class AnimaisForm(forms.Form):
    class Meta:
        model = Animal
        fields = '__all__'
