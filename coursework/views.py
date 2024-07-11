from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from coursework.forms import ClientForm, MessageForm
from coursework.models import Client, Message


class FirstPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "coursework/first_page.html")


class ClientListView(ListView):
    """Вьюшка списка клиентов"""
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


class MessageListView(ListView):
    """Вьюшка списка сообщений"""
    model = Message


class MessageDetailView(DetailView):
    """Вьюшка одного сообщения"""
    model = Message


class MessageCreateView(CreateView):
    """Вьюшка создания нового сообщения"""
    model = Client
    form_class = MessageForm

    def get_success_url(self):
        return reverse('coursework:message_detail', args=[self.object.pk])


class MessageUpdateView(UpdateView):
    """Вьюшка редактирования сообщения"""
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse('coursework:message_detail', args=[self.object.pk])


class MessageDeleteView(DeleteView):
    """Вьюшка удаления сообщения"""
    model = Message
    success_url = reverse_lazy("coursework:message_list")
