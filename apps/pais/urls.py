from django.conf.urls import url, include
from apps.pais.views import index, pais_view, pais_list, pais_edit, pais_delete
urlpatterns = [
    url(r'^$', index ,name='index'),
    url(r'^adicionar$', pais_view,name='pais_crear'),
    url(r'^listar$', pais_list,name='pais_listar'),
    url(r'^editar/(?P<id_pais>\d+)/$', pais_edit,name='pais_editar'),
    url(r'^eliminar/(?P<id_pais>\d+)/$', pais_delete,name='pais_eliminar'),
]
