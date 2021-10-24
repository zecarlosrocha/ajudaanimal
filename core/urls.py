from django.urls import path

from .views import IndexView, EntidadesView, CreateEntidadeView, UpdateEntidadeView, DeleteEntidadeView, \
                   AnimaisView, CreateAnimalView, UpdateAnimalView, DeleteAnimalView, \
                   PesquisaAnimaisView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('entidades/', EntidadesView.as_view(), name='entidades'),
    path('entidades/add/', CreateEntidadeView.as_view(), name='add_entidade'),
    path('entidades/<int:pk>/update/', UpdateEntidadeView.as_view(), name='upd_entidade'),
    path('entidades/<int:pk>/delete/', DeleteEntidadeView.as_view(), name='del_entidade'),
    path('animais/', AnimaisView.as_view(), name='animais'),
    path('animais/add/', CreateAnimalView.as_view(), name='add_animal'),
    path('animais/<int:pk>/update/', UpdateAnimalView.as_view(), name='upd_animal'),
    path('animais/<int:pk>/delete/', DeleteAnimalView.as_view(), name='del_animal'),
    path('adocao/', PesquisaAnimaisView.as_view(), name='pesquisa_animais'),
]