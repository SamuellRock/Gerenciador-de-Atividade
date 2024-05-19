from django.contrib import admin
from django.urls import path,include
from .views import teste
from cadastro import urls as cadastro_urls
from perfis import urls as perfis_urls

#TODO Upgrade para home/
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', teste, name='teste'),
    path('', include(cadastro_urls)),
    path('', include(perfis_urls)),
]
