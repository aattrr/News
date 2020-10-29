from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.forms import RegisterForm
from app_users.models import Profile, News
from .forms import RegisterForm


class LoginView(LoginView):
    template_name = 'djregistration/login.html'


class LogoutView(LogoutView):
    template_name = 'djregistration/logout.html'


class MainPage(TemplateView):
    template_name = "djregistration/main.html"


class PersonalInf(TemplateView):
    """Сраница персональной информации"""
    template_name = "djregistration/personal_inf.html"

    def get_context_data(self, **kwargs):
        """Получаем колличество опубликованных новостей"""
        context = super(PersonalInf, self).get_context_data(**kwargs)
        select_user = News.objects.filter(user=self.request.user)
        context['count_news'] = select_user.count()
        return context


def register(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            town = form.cleaned_data.get('town')
            tel = form.cleaned_data.get('tel')
            Profile.objects.create(
                user=user,
                town=town,
                tel=tel
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Ошибка Регистрации')
    else:
        form = RegisterForm()
    return render(request, 'djregistration/register.html', {'form': form})
