from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from coursework.forms import ClientForm, MessageForm, MailingForm
from coursework.models import Client, Message, Mailing, MailingStatus, Attempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class FirstPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "coursework/first_page.html")


class ClientListView(LoginRequiredMixin, ListView):
    """Вьюшка списка клиентов"""
    model = Client

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        return Client.objects.filter(created_user=self.request.user)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Вьюшка редактирования клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("coursework:client_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.created_user or self.request.user.is_superuser:
            return self.object
        else:
            return PermissionDenied


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Вьюшка создания клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("coursework:client_list")

    def form_valid(self, form):
        client = form.save()
        client.created_user = self.request.user
        form.save()
        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("coursework:client_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.created_user or self.request.user.is_superuser:
            return self.object
        else:
            return PermissionDenied


class MessageListView(LoginRequiredMixin, ListView):
    """Вьюшка списка сообщений"""
    model = Message

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Message.objects.all()
        return Message.objects.filter(created_user=self.request.user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Вьюшка одного сообщения"""
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Вьюшка создания нового сообщения"""
    model = Client
    form_class = MessageForm

    def get_success_url(self):
        return reverse('coursework:message_detail', args=[self.object.pk])

    def form_valid(self, form):
        message = form.save()
        message.created_user = self.request.user
        form.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Вьюшка редактирования сообщения"""
    model = Message
    form_class = MessageForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.created_user or self.request.user.is_superuser:
            return self.object
        else:
            return PermissionDenied

    def get_success_url(self):
        return reverse('coursework:message_detail', args=[self.object.pk])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Вьюшка удаления сообщения"""
    model = Message
    success_url = reverse_lazy("coursework:message_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.created_user or self.request.user.is_superuser:
            return self.object
        else:
            return PermissionDenied


class MailingListView(LoginRequiredMixin, ListView):
    """Вьюшка списка рассылок"""
    model = Mailing

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.has_perm("coursework.view_mailing"):
            return Mailing.objects.all()
        return Mailing.objects.filter(created_user=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Вьюшка создания новой рассылки"""
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('coursework:mailing_detail', args=[self.object.pk])

    def form_valid(self, form):
        mailing = form.save()
        mailing.status = MailingStatus.objects.get(status="Создана")
        mailing.created_user = self.request.user
        form.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Вьюшка редактирования рассылки"""
    model = Mailing
    form_class = MailingForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.created_user or self.request.user.is_superuser:
            return self.object
        else:
            return PermissionDenied

    def get_success_url(self):
        return reverse('coursework:mailing_detail', args=[self.object.pk])


class MailingDetailView(LoginRequiredMixin, DetailView):
    """Вьюшка одной рассылки"""
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Вьюшка удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy("coursework:mailing_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.created_user or self.request.user.is_superuser:
            return self.object
        else:
            return PermissionDenied


def activated_mailing(request, pk):
    """Вьюшка активации рассылки"""
    mailing = get_object_or_404(Mailing, pk=pk)
    if mailing.enable:
        mailing.enable = False
        mailing.status = MailingStatus.objects.get(status="Завершена")
    else:
        mailing.enable = True
        mailing.status = MailingStatus.objects.get(status="Запущена")

    mailing.save()

    return redirect(reverse('coursework:mailing_detail', args=[pk]))


class AttemptListView(LoginRequiredMixin, ListView):
    """Вьюшка попытки отправки рассылки"""
    model = Attempt

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(mailing=self.kwargs['pk'])
        return queryset
