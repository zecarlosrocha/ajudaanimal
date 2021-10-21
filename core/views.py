from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Entidade


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
    model = Entidade
    template_name = 'entidade_del.html'
    success_url = reverse_lazy('entidades')
