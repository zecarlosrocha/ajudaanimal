from django.urls import path, include
from .views import IndexView, EntidadesView, CreateEntidadeView, UpdateEntidadeView, DeleteEntidadeView, \
                   AnimaisView, CreateAnimalView, UpdateAnimalView, DeleteAnimalView, \
                   PesquisaAnimaisView, ExemploView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('entidades/', EntidadesView.as_view(), name='entidades'),
    path('exemplo/', ExemploView.as_view(), name='exemplo'),
    path('entidades/add/', CreateEntidadeView.as_view(), name='add_entidade'),
    path('entidades/<int:pk>/update/', UpdateEntidadeView.as_view(), name='upd_entidade'),
    path('entidades/<int:pk>/delete/', DeleteEntidadeView.as_view(), name='del_entidade'),
    path('animais/', AnimaisView.as_view(), name='animais'),
    path('animais/add/', CreateAnimalView.as_view(), name='add_animal'),
    path('animais/<int:pk>/update/', UpdateAnimalView.as_view(), name='upd_animal'),
    path('animais/<int:pk>/delete/', DeleteAnimalView.as_view(), name='del_animal'),
    path('adocao/', PesquisaAnimaisView.as_view(), name='pesquisa_animais'),
    path('contas/', include('django.contrib.auth.urls')),
]