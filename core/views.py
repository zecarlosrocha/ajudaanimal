from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Entidade, Animal
from core.forms.forms import AnimalForm, AnimaisForm
from django.db.models import Q


class IndexView(ListView):
    model = Entidade
    template_name = 'index.html'
    success_url = reverse_lazy('index')


class EntidadesView(ListView):
    template_name = 'entidades.html'
    model = Entidade
    paginate_by = 4
    ordering = 'nome'


class CreateEntidadeView(CreateView):
    model = Entidade
    template_name = 'entidade_form.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('entidades')


class UpdateEntidadeView(UpdateView):
    model = Entidade
    template_name = 'entidade_form.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('entidades')


class DeleteEntidadeView(DeleteView):
    model = Animal
    template_name = 'entidade_del.html'
    success_url = reverse_lazy('entidades')


class AnimaisView(ListView):
    model = Animal
    template_name = 'animais.html'
    form_class = AnimaisForm
    paginate_by = 10
    ordering = 'nome'


class CreateAnimalView(CreateView):
    model = Animal
    template_name = 'animal_form.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animais')


class UpdateAnimalView(UpdateView):
    model = Animal
    template_name = 'animal_form.html'
    fields = ['nome', 'idade', 'raca', 'entidade', 'imagem']
    success_url = reverse_lazy('animais')


class DeleteAnimalView(DeleteView):
    model = Animal
    template_name = 'animal_del.html'
    success_url = reverse_lazy('animais')


class PesquisaAnimaisView(ListView):
    template_name = 'animais_pesquisa.html'
    model = Animal
    context_object_name = 'object'
    paginate_by = 10
    ordering = 'nome'

    def get_queryset(self):
        search = self.request.GET.get('src')
        if search:
            qs = self.model.objects.filter(Q(entidade__nome__icontains=search) | Q(nome__icontains=search) | Q(raca__nome__icontains=search))
        else:
            qs = self.model.objects.all()
        qs = qs.order_by("-nome")   # you don't need this if you set up your ordering on the model
        return qs

