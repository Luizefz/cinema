from django.views.generic import ListView

from .models import Filme

class FilmeListView(ListView):
    model = Filme
    template_name = 'filme_list.html'