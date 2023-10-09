from django import views
from django.urls import path
from .views import Login_a_Pagina, RegistroPagina, UsuarioEdicion, CambioClave, InicioView ,galeriaComedia, ComediaDetalle, ComediaUpdate, PeliculasCreacion,ComediaDelete, GaleriaTerror, TerrorDetalle, TerrorUpdate,TerrorDelete, GaleriaAccion,AccionDetalle,AccionrUpdate,AccionDelete,GaleriaRomanticas,RomanticasDetalle,RomanticasUpdate, RomanticasDelete, GaleriaSuspenso, SuspensoDetalle, SuspensoUpdate,SuspensoDelete, GaleriaOtras,OtrasDetalle, OtrasUpdate, OtrasDelete, ComentarioPagina, AvatarFormulario, agregaravatar
from django.contrib.auth.views import  LogoutView
from . import views


urlpatterns = [
    #urls de usuario y registro y login.
    path('', InicioView.as_view(), name='inicio'),
    path('login/', Login_a_Pagina.as_view(), name='login'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('ClavesCambio/', CambioClave.as_view(), name='cambiar_password'),
    path('ClavesExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('Avatar/' , views.agregaravatar, name='Avatar'),
    
    
    #asesorios de galeria
    
    path('galeriaComedia/', galeriaComedia.as_view(), name='comedia'),
    path('GaleriaTerror/', GaleriaTerror.as_view(), name='terror'),
    path('GaleriaAccion/', GaleriaAccion.as_view(), name='accion'),
    path('GaleriaRomanticas/', GaleriaRomanticas.as_view(), name='romanticas'),
    path('GaleriaSuspenso/', GaleriaSuspenso.as_view(), name='suspenso'),
    path('GaleriaOtras/', GaleriaOtras.as_view(), name='otraspeliculas'),
   
    
    
    #detalles de peliculas
    
    path('comediaDetalle/<int:pk>/', ComediaDetalle.as_view(), name='comedias'),
    path('TerrorDetalle/<int:pk>/', TerrorDetalle.as_view(), name='terror'),
    path('accionDetalle/<int:pk>/', AccionDetalle.as_view(), name='accion'),
    path('RomanticasDetalle/<int:pk>/', RomanticasDetalle.as_view(), name='romanticas'),
    path('SuspensoDetalle/<int:pk>/', SuspensoDetalle.as_view(), name='suspenso'),
    path('OtrasDetalle/<int:pk>/', OtrasDetalle.as_view(), name='otraspeliculas'),
    
    
    #Temas de Edicion
    
    path('comediaEdicion/<int:pk>/', ComediaUpdate.as_view(), name='comedia_editar'),
    path('terrorEdicion/<int:pk>/', TerrorUpdate.as_view(), name='terror_editar'),
    path('accionEdicion/<int:pk>/', AccionrUpdate.as_view(), name='accion_editar'),
    path('RomanticasEdicion/<int:pk>/', RomanticasUpdate.as_view(), name='romanticas_editar'),
    path('SuspensoUpdate/<int:pk>/', SuspensoUpdate.as_view(), name='suspenso_editar'),
    path('OtrasUpdate/<int:pk>/', OtrasUpdate.as_view(), name='suspenso_editar'),
    
    
    #Eliminacion
    
    path('comediaBorrado/<int:pk>/', ComediaDelete.as_view(), name='comedia_eliminar'),
    path('terrorBorrado/<int:pk>/', TerrorDelete.as_view(), name='terror_eliminar'),
    path('accionBorrado/<int:pk>/', AccionDelete.as_view(), name='accion_eliminar'),
    path('romanticasBorrado/<int:pk>/', RomanticasDelete.as_view(), name='romanticas_eliminar'),
    path('suspensoBorrado/<int:pk>/', SuspensoDelete.as_view(), name='suspenso_eliminar'),
    path('OtrasBorrado/<int:pk>/', OtrasDelete.as_view(), name='otras_eliminar'),
    
    
    
    #Creacion de peliculas
    
    path('PeliculaCreacion/', PeliculasCreacion.as_view(), name='nuevo'),
    
    
    #Crear Comentario por pelicula 
    
    path('comediaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('terrorDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('accionDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('romanticasDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('suspensoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otrasDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    
    #algo sobre mi y mi vida
    path('algosobremi/', views.about, name='conoceme'),

     
]