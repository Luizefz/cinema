from django.urls import path
from .views import FilmeAPIView


urlpatterns = [
    path('', FilmeAPIView.as_view()),
]