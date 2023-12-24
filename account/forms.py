from django import forms


class LoginForm(forms.Form):
    login = forms.CharField()  # обычный CharField
    password = forms.CharField(
        widget=forms.PasswordInput)  # widget PasswordInput - означает встроенная функция ввода пароля
