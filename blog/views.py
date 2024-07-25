from datetime import datetime
import pytz, random
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required, login_required
from blog.forms import BlogForm
from blog.models import Blog
from pytils.translit import slugify
from django.views.decorators.cache import cache_page
from config import settings
from config.settings import CACHE_ENABLED
from coursework.models import Mailing, Client



class BlogListView(LoginRequiredMixin, ListView):
    """Вьюшка списка статей"""
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if CACHE_ENABLED:
            key = f'blog_list'
            blog_list = cache.get(key)
            if blog_list is None:
                blog_list = Blog.objects.all()
                cache.set(key, blog_list)
        else:
            blog_list = Blog.objects.all()

        context['blog_list'] = blog_list
        return context

    def get_queryset(self):
        if self.request.user.has_perm('blog.can_public') or self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.filter(is_public=True)


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Вьюшка создания новой статьи"""
    model = Blog
    form_class = BlogForm
    permission_required = ('blog.add_blog',)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.object.slug])

    def form_valid(self, form):
        blog = form.save()
        blog.author = self.request.user
        blog.slug = slugify(blog.title)
        blog.save()
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Вьюшка удаления статьи"""
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    permission_required = ('blog.delete_blog',)


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Вьюшка редактирования статьи"""
    model = Blog
    form_class = BlogForm
    permission_required = ('blog.change_blog',)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.object.slug])


class BlogDetailView(LoginRequiredMixin, DetailView):
    """Вьюшка одной статьи"""
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.is_public:
            self.object.view_count += 1
            self.object.save()
        return self.object


@permission_required("blog.can_public")
@login_required
def publish_blog(request, slug):
    """Функция публикации статьи"""
    blog = get_object_or_404(Blog, slug=slug)
    if blog.is_public:
        blog.is_public = False
    else:
        blog.is_public = True
        zone = pytz.timezone(settings.TIME_ZONE)
        current_datetime = datetime.now(zone)
        blog.publicated_at = current_datetime
    blog.save()
    return redirect(reverse('blog:blog_detail', args=[slug]))


@cache_page(60)
def general_page(request):
    """Общая страница сайта"""
    active_mailing = len(Mailing.objects.filter(enable=True))
    all_mailing = len(Mailing.objects.all())
    all_blogs = Blog.objects.filter(is_public=True)
    clients = Client.objects.all()
    context = {
        "active_mailing": active_mailing,
        "all_mailing": all_mailing,
        "clients": len(clients),
    }
    if all_blogs:
        random_blog = random.choices(all_blogs, k=3)
        context["first_blog"] = random_blog[0]
        context["second_blog"] = random_blog[1]
        context["third_blog"] = random_blog[2]
    else:
        random_blog = []
        context["first_blog"] = random_blog
        context["second_blog"] = random_blog
        context["third_blog"] = random_blog

    return render(request, "blog/general_page.html", context)

