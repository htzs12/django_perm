from django.test import TestCase
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import View
from .forms import UserTestForm


class FormTestView(View):
    def get(self, request):
        test_form = UserTestForm()
        return render(request, 'system/users/form_test.html', {'test_form': test_form})

    def post(self, request):
        test_form = UserTestForm(request.POST)
        ret = dict(test_form=test_form)
        if test_form.is_valid():
            return HttpResponseRedirect('/')
        return render(request, 'system/users/form_test.html', ret)

