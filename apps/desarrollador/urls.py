from django.conf.urls import url, include
from apps.desarrollador.views import index_desarrollador,desarrollador_view,desarrollador_list
urlpatterns = [
  url(r'^$',index_desarrollador, name='index_desarrollador'),
  url(r'^adicionar$', desarrollador_view, name='desarrollador_crear'),
  url(r'^listar$', desarrollador_list, name='desarrollador_listar'),
]
