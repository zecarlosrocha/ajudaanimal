from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Entidade


class IndexView(ListView):
    models = Entidade
    template_name = 'index.html'
    queryset = Entidade.objects.all()
    context_object_name = 'entidades'


class CreateEntidadeView(CreateView):
    model = Entidade
    template_name = 'entidade_form.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('index')


class UpdateEntidadeView(UpdateView):
    model = Entidade
    template_name = 'entidade_form.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('index')


class DeleteEntidadeView(DeleteView):
    model = Entidade
    template_name = 'entidade_del.html'
    success_url = reverse_lazy('index')
