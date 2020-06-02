from django.conf.urls import url, include
from apps.clasificacion.views import index_clasificacion
urlpatterns = [
 url(r'^$',index_clasificacion)
]
