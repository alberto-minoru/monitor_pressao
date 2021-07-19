from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Pressao


class PressaoListView(ListView):
    model = Pressao
    template_name = 'registros/registros_list.html'


class PressaoDetailView(DetailView):
    model = Pressao
    template_name = 'registros/registro_detail.html'


class PressaoCreateView(CreateView):
    model = Pressao
    template_name = 'registros/registro_new.html'
    fields = ['pessoa', 'sis', 'dia', 'pul']
