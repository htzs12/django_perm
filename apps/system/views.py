from django.shortcuts import render
from django.views.generic.base import View
from .forms import LoginForm
from django.http.response import HttpResponseRedirect


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    """
    登录
    """
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'system/users/login.html')
        else:
            return HttpResponseRedirect('/')


