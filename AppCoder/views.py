from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Peliculas, Comentario, Avatar
from .forms import ActualizacionPeliculas, FormularioCambioPassword, FormularioEdicion, FormularioNuevoPeliculas, FormularioRegistroUsuario, FormularioComentario, AvatarFormulario

#Agregar un avatar a su perfil

def agregaravatar(request):
    
    if request.method=="POST":
        form = AvatarFormulario(request.post, request.FILES)
        
        if form.is_valid():
            
            usuarioactual = User.objects.get(username=request.user)
            
            avatar = Avatar(usuario=usuarioactual, imagen=form.cleaned_data["imagen"])
            
            avatar.seve()
            
            return render(request, 'AppCoder/inicio.html')
        else:
            form = AvatarFormulario
            
        return render(request,"AppCoder/avatar.html", {"formulario":form})



# Create your views here.

class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'AppCoder/Inicio.html'
    
class Login_a_Pagina(LoginView):
    template_name = 'AppCoder/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')
    
class RegistroPagina(FormView):
    template_name = 'AppCoder/registrar.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('incio')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'AppCoder/edicionPerfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user

class CambioClave(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppCoder/clavesCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'AppCoder/clavesExitoso.html', {})


#galeria de peliculas = Comedia

class galeriaComedia(LoginRequiredMixin, ListView):
    context_object_name = 'comedias'
    queryset = Peliculas.objects.filter(genero__startswith='comedias')
    template_name = 'AppCoder/galeriaComedia.html'
    login_url = '/login/'
 
class ComediaDetalle(LoginRequiredMixin, DetailView):
    model = Peliculas
    context_object_name = 'comedias' 
    template_name = 'AppCoder/ComediaDetalle.html'

class ComediaUpdate(LoginRequiredMixin, UpdateView):
    model = Peliculas
    form_class = ActualizacionPeliculas
    success_url = reverse_lazy('comedias')
    context_object_name = 'comedias'
    template_name = 'AppCoder/ComediaEdicion.html'

class ComediaDelete(LoginRequiredMixin, DeleteView):
    model = Peliculas
    success_url = reverse_lazy('comedias')
    context_object_name = 'comedias'
    template_name = 'AppCoder/comediasBorrado.html'

#galeria de peliculas = terror

class GaleriaTerror(LoginRequiredMixin, ListView):
    context_object_name = 'terror'
    queryset = Peliculas.objects.filter(genero__startswith='terror')
    template_name = 'AppCoder/GaleriaTerror.html'
    login_url = '/login/'
    
class TerrorDetalle(LoginRequiredMixin, DetailView):
    model = Peliculas
    context_object_name = 'terror'
    template_name = 'AppCoder/terrorDetalle.html'
    
    
class TerrorUpdate(LoginRequiredMixin, UpdateView):
    model = Peliculas
    form_class = ActualizacionPeliculas
    success_url = reverse_lazy('terror')
    context_object_name = 'terror'
    template_name = 'AppCoder/TerrorUpdate.html'

class TerrorDelete(LoginRequiredMixin, DeleteView):
    model = Peliculas
    success_url = reverse_lazy('terror')
    context_object_name = 'terror'
    template_name = 'AppCoder/terrorBorrado.html'
    
    
#galeria de peliculas = Accion
  
class GaleriaAccion(LoginRequiredMixin, ListView):
    context_object_name = 'accion'
    queryset = Peliculas.objects.filter(genero__startswith='accion')
    template_name = 'AppCoder/GaleriaAccion.html'
    login_url = '/login/'  
    
class AccionDetalle(LoginRequiredMixin, DetailView):
    model = Peliculas
    context_object_name = 'accion'
    template_name = 'AppCoder/AccionDetalle.html'
    
class AccionrUpdate(LoginRequiredMixin, UpdateView):
    model = Peliculas
    form_class = ActualizacionPeliculas
    success_url = reverse_lazy('accion')
    context_object_name = 'accion'
    template_name = 'AppCoder/AccionrUpdate.html'
    
    
class AccionDelete(LoginRequiredMixin, DeleteView):
    model = Peliculas
    success_url = reverse_lazy('accion')
    context_object_name = 'accion'
    template_name = 'AppCoder/accionBorrado.html'
    
    

#galeria de peliculas = romanticas
    
class GaleriaRomanticas(LoginRequiredMixin, ListView):
    context_object_name = 'romanticas'
    queryset = Peliculas.objects.filter(genero__startswith='romanticas')
    template_name = 'AppCoder/GaleriaRomanticas.html'
    login_url = '/login/'   
    
class RomanticasDetalle(LoginRequiredMixin, DetailView):
    model = Peliculas
    context_object_name = 'romanticas'
    template_name = 'AppCoder/RomanticasDetalle.html'

class RomanticasUpdate(LoginRequiredMixin, UpdateView):
    model = Peliculas
    form_class = ActualizacionPeliculas
    success_url = reverse_lazy('romanticas')
    context_object_name = 'romanticas'
    template_name = 'AppCoder/RomanticasrUpdate.html'
    

class RomanticasDelete(LoginRequiredMixin, DeleteView):
    model = Peliculas
    success_url = reverse_lazy('romanticas')
    context_object_name = 'romanticas'
    template_name = 'AppCoder/RomanticasBorrado.html'
    
    
#galeria de peliculas = suspenso

class GaleriaSuspenso(LoginRequiredMixin, ListView):
    context_object_name = 'suspenso'
    queryset = Peliculas.objects.filter(genero__startswith='suspenso')
    template_name = 'AppCoder/GaleriaSuspenso.html'
    login_url = '/login/'   
    
class SuspensoDetalle(LoginRequiredMixin, DetailView):
    model = Peliculas
    context_object_name = 'suspenso'
    template_name = 'AppCoder/SuspensoDetalle.html'

class SuspensoUpdate(LoginRequiredMixin, UpdateView):
    model = Peliculas
    form_class = ActualizacionPeliculas
    success_url = reverse_lazy('suspenso')
    context_object_name = 'suspenso'
    template_name = 'AppCoder/SuspensoUpdate.html'
    

class SuspensoDelete(LoginRequiredMixin, DeleteView):
    model = Peliculas
    success_url = reverse_lazy('suspenso')
    context_object_name = 'suspenso'
    template_name = 'AppCoder/suspensoBorrado.html'
    

#galeria de peliculas = otras   

class GaleriaOtras(LoginRequiredMixin, ListView):
    context_object_name = 'otras'
    queryset = Peliculas.objects.filter(genero__startswith='otras')
    template_name = 'AppCoder/GaleriaOtras.html'
    login_url = '/login/'   

class OtrasDetalle(LoginRequiredMixin, DetailView):
    model = Peliculas
    context_object_name = 'otras'
    template_name = 'AppCoder/otrasDetalle.html'
    
class OtrasUpdate(LoginRequiredMixin, UpdateView):
    model = Peliculas
    form_class = ActualizacionPeliculas
    success_url = reverse_lazy('otras')
    context_object_name = 'otras'
    template_name = 'AppCoder/OtrasUpdate.html'
    
class OtrasDelete(LoginRequiredMixin, DeleteView):
    model = Peliculas
    success_url = reverse_lazy('otras')
    context_object_name = 'otras'
    template_name = 'AppCoder/otrasBorrado.html'   


# CREACION PELICULAS

class PeliculasCreacion(LoginRequiredMixin, CreateView):
    model = Peliculas
    form_class = FormularioNuevoPeliculas
    success_url = reverse_lazy('inicio')
    template_name = 'AppCoder/PeliculasCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PeliculasCreacion, self).form_valid(form)

#COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppCoder/comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'AppCoder/acercademi.html', {})



