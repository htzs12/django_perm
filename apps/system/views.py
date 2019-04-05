# __author__ : htzs
# __time__   : 19-4-5 上午9:05


from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin


class  SystemView(LoginRequiredMixin, View):
    """
    系统设置页
    """
    def get(self, request):
        return render(request, 'system/system_index.html')