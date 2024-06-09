from django.contrib import admin
from django.urls import path,include
from .views import teste
from cadastro import urls as cadastro_urls
from perfis import urls as perfis_urls
from AppHome import urls as appHome_urls
from django.conf.urls import handler400, handler403, handler404


#TODO Upgrade para home/
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', teste, name='teste'),
    path('', include(cadastro_urls)),
    path('', include(perfis_urls)),
    path('', include(appHome_urls)),
]

handler404 = "AppHome.views.erro_page"
handler403 = "AppHome.views.erro_page"
handler400 = "AppHome.views.erro_page"