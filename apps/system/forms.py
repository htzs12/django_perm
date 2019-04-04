# __author__ : htzs
# __time__   : 19-4-4 下午11:15

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages='请填写用户名')
    password = forms.CharField(required=True, error_messages='请填写密码')