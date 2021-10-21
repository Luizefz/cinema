from django.shortcuts import render
from rest_framework import generics
from filmes.models import Filme
from .serializers import FilmeSerializer

class FilmeAPIView(generics.ListAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer