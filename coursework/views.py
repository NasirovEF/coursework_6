from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from coursework.forms import ClientForm, MessageForm, MailingForm
from coursework.models import Client, Message, Mailing, MailingStatus, Attempt


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


class MailingListView(ListView):
    """Вьюшка списка рассылок"""
    model = Mailing


class MailingCreateView(CreateView):
    """Вьюшка создания новой рассылки"""
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('coursework:mailing_detail', args=[self.object.pk])

    def form_valid(self, form):
        mailing = form.save()
        mailing.status = MailingStatus.objects.get(status="Создана")
        form.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    """Вьюшка редактирования рассылки"""
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('coursework:mailing_detail', args=[self.object.pk])


class MailingDetailView(DetailView):
    """Вьюшка одной рассылки"""
    model = Mailing


class MailingDeleteView(DeleteView):
    """Вьюшка удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy("coursework:mailing_list")


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


class AttemptListView(ListView):
    """Вьюшка попытки отправки рассылки"""
    model = Attempt

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(mailing=self.kwargs['pk'])
        return queryset
