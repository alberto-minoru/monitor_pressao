from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pressao


class PressaoListView(LoginRequiredMixin, ListView):
    model = Pressao
    template_name = 'registros/registros_list.html'
    paginate_by = 100

    def get_queryset(self):
        return self.model.objects.filter(pessoa=self.request.user).order_by('-data')


class PressaoDetailView(LoginRequiredMixin, DetailView):
    model = Pressao
    template_name = 'registros/registro_detail.html'


class PressaoCreateView(LoginRequiredMixin, CreateView):
    model = Pressao
    template_name = 'registros/registro_new.html'
    fields = ['sis', 'dia', 'pul']

    def form_valid(self, form):
        form.instance.pessoa = self.request.user
        form.instance.data = datetime.now()
        return super().form_valid(form)


class PressaoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pressao
    template_name = 'registros/registro_edit.html'
    fields = ['sis', 'dia', 'pul']

    def test_func(self):
        obj = self.get_object()
        return obj.pessoa == self.request.user


class PressaoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pressao
    template_name = 'registros/registro_delete.html'
    success_url = reverse_lazy('registros_list')

    def test_func(self):
        obj = self.get_object()
        return obj.pessoa == self.request.user
