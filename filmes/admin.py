from django.contrib import admin
from .models import Categoria, Filme


class FilmeAdmin(admin.ModelAdmin):
    fields = ('titulo', 'capa')
    list_display = ['titulo', 'image_capa', 'get_categoria']
    readonly_fields = ('categoria', 'image_capa')

    def get_categoria(self, obj):
        return obj.categoria.genero
    get_categoria.short_description = 'categoria'


admin.site.register(Filme, FilmeAdmin)
admin.site.register(Categoria)


# Register your models here.
