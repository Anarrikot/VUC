from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import AddSolderForm, RegisterUserForm, LoginUserForm
from .models import Solder
from .utils import menu, DataMixin
# Create your views here.

class SolderHome(DataMixin, ListView):
    model = Solder
    template_name = 'soldiers/index.html'
    context_object_name = 'soldiers'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title= 'Преподаватели')
        return {**context, **c_def}

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'soldiers/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'soldiers/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


def about(request):
    return render(request, 'soldiers/about.html', {'menu':
menu,'title': 'О сайте'})

def logout_user(request):
    logout(request)
    return redirect('login')

class AddSolder(CreateView):
    form_class = AddSolderForm
    template_name = 'soldiers/addsolder.html'


class ShowSoldier(DataMixin, DetailView):
    model = Solder
    template_name = 'soldiers/soldier.html'
    slug_url_kwarg = 'so_slug'
    context_object_name = 'so'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Преподаватель')
        return {**context, **c_def}

