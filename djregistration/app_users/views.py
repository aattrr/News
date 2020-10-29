from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from app_users.models import News, Comment, User, Profile, Metatag
from .forms import NewsForm, CommentForm


class NewsList(ListView):
    """ Вывод списка новостей """
    model = News

    def get_context_data(self, **kwargs):
        """Переопределение getcontextdata для сортировки по созданию активных объявлений"""
        context = super(NewsList, self).get_context_data(**kwargs)
        context['object_list'] = News.objects.filter(status=True).order_by('-create_at')
        context['cloud_tags'] = Metatag.objects.all
        return context


class NewsFilter(ListView):
    """Фильтрация новостей по тегу"""
    model = News
    template_name = 'app_users/filter_news.html'
    def get_context_data(self, **kwargs):
        context = super(NewsFilter, self).get_context_data(**kwargs)
        select_tag = Metatag.objects.get(id=self.kwargs['pk'])
        context['filtered_news'] = News.objects.filter(metatag=select_tag).order_by('-create_at')
        context['select_tag'] = select_tag
        return context


class NewsDetail(DetailView):
    """Вывод страницы детального описания новости"""
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        select_news = News.objects.get(id=self.kwargs['pk'])
        context['comment_list'] = Comment.objects.filter(news=select_news)
        return context


class CreateNews(CreateView):
    """Создание новости"""
    form_class = NewsForm
    template_name = 'app_users/add_news.html'

    @method_decorator(permission_required('app_users.add_news', raise_exception=True))
    def dispatch(self, request):
        """Устанавливаем разрешения на добавление новости"""
        return super(CreateNews, self).dispatch(request)

    def form_valid(self, form):
        """Валидация формы, сохранение текущего пользователя, если авторизован"""
        user = self.request.user
        if user.is_authenticated:
            news = form.save(commit=False)
            news.user = user
            news.save()
            return super(CreateNews, self).form_valid(form)


class EditNews(UpdateView):
    """Редактирование новости"""
    model = News
    template_name = 'app_users/edit_news.html'
    success_url = reverse_lazy('news_list')
    fields = ['title', 'description', 'status']


class CreateComment(CreateView):
    """Создание комментария"""
    form_class = CommentForm
    template_name = 'app_users/add_comment.html'

    def form_valid(self, form):
        user = self.request.user
        news = News.objects.get(id=self.kwargs['pk'])
        if user.is_authenticated:
            new_comment = form.save(commit=False)
            new_comment.news = news
            new_comment.user = user
            new_comment.save()
            return redirect('news_list')
        else:
            new_comment = form.save(commit=False)
            new_comment.news = news
            new_comment.save()
            return redirect('news_list')
