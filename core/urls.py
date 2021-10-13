from django.urls import path

from .views import IndexView, CreateEntidadeView, UpdateEntidadeView, DeleteEntidadeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateEntidadeView.as_view(), name='add_entidade'),
    path('<int:pk>/update/', UpdateEntidadeView.as_view(), name='upd_entidade'),
    path('<int:pk>/delete/', DeleteEntidadeView.as_view(), name='del_entidade'),
]