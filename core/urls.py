from django.urls import path

from .views import IndexView, EntidadesView, CreateEntidadeView, UpdateEntidadeView, DeleteEntidadeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('entidades/', EntidadesView.as_view(), name='entidades'),
    path('entidades/add/', CreateEntidadeView.as_view(), name='add_entidade'),
    path('entidades/<int:pk>/update/', UpdateEntidadeView.as_view(), name='upd_entidade'),
    path('entidades/<int:pk>/delete/', DeleteEntidadeView.as_view(), name='del_entidade'),
]