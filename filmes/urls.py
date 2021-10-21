from django.urls import path
from .views import FilmeListView

urlpatterns = [
    path('', FilmeListView.as_view(), name='home'),
]