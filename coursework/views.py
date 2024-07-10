from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from coursework.forms import ClientForm
from coursework.models import Client


class FirstPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "coursework/first_page.html")


class ClientListView(ListView):
    """Вьюшка списка клиентов"""
    model = Client


class ClientDetailView(DetailView):
    """Вьюшка одного клиента"""
    model = Client



class ClientUpdateView(UpdateView):
    """Вьюшка редактирования клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("coursework:client_list")


class ClientCreateView(CreateView):
    """Вьюшка создания клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("coursework:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("coursework:client_list")

