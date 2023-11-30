from django.urls import path
from publicar import views as publicar_view
from django.conf import settings
urlpatterns = [
    path('',publicar_view.Inicio,name='Inicio'),
    path('home',publicar_view.Inicio,name='Inicio'),
    path('about.html',publicar_view.Public,name='Publicar'),
    path('mn',publicar_view.men,name='Hombres'),
    path('categoria',publicar_view.crear, name='crear'),
    path('editar/<int:n>',publicar_view.editar, name='editar'),
    path('borr/<int:n>',publicar_view.borr, name='borr'),
    path('women',publicar_view.women,name='Mujeres'),
    path('logout/',publicar_view.exit, name='Salir'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
