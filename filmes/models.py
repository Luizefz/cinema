from django.db import models
from django.utils.safestring import mark_safe


class Categoria(models.Model):
    genero = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.genero


class Filme(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    resenha = models.TextField()
    diretor = models.CharField(max_length=250, null=False)
    produtora = models.CharField(max_length=300, null=True)
    capa = models.ImageField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def image_capa(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.capa.url))
    image_capa.short_description = 'capa'
    image_capa.allow_tags = True
