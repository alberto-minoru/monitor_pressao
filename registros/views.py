from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    fields = ['sis', 'dia', 'pul']

    def form_valid(self, form):
        form.instance.pessoa = self.request.user
        return super().form_valid(form)


class PressaoUpdateView(UpdateView):
    model = Pressao
    template_name = 'registros/registro_edit.html'
    fields = ['sis', 'dia', 'pul']


class PressaoDeleteView(DeleteView):
    model = Pressao
    template_name = 'registros/registro_delete.html'
    success_url = reverse_lazy('registros_list')
