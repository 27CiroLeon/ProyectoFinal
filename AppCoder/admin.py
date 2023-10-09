from django.contrib import admin
from .models import Peliculas, Comentario, Avatar

# Register your models here.


admin.site.register(Peliculas)
admin.site.register(Comentario)
admin.site.register(Avatar)