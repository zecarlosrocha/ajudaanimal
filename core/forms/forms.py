from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import Animal, Entidade


# DataFlair
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'idade', 'raca', 'imagem']


class AnimaisForm(forms.Form):
    class Meta:
        model = Animal
        fields = '__all__'


class EntidadeModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Entidade
        fields = ['email', 'nome', 'fone', 'cidade', 'uf', 'site', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EntidadeChangeModelForm(forms.ModelForm):

    class Meta:
        model = Entidade
        fields = ['email', 'nome', 'fone', 'cidade', 'uf', 'site']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EntidadeCreateForm(UserCreationForm):
    class Meta:
        model = Entidade
        fields = ('nome', 'fone', 'cidade', 'uf')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class EntidadeChangeForm(UserChangeForm):
    class Meta:
        model = Entidade
        fields = ('nome', 'fone', 'cidade', 'uf')
