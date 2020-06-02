from django.conf.urls import url, include
from apps.juego.views import index_juego
urlpatterns = [
 url(r'^$',index_juego)
]
