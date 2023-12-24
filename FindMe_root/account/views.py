from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})  # это у нас всё декортатор
# у нас как только мы входим на наш рабочий стол сайта, он проверяется на то, аутентифирован ли пользователь




def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():  # функция пайтона, проверка на валидность данных
            cd = form.cleaned_data  # cd - cleaned data - удалить значения
            user = authenticate(request, login=cd['login'], password=cd['password'])  # функция пайтона, которая
            # проверяет данные и возвращает объект user

        if user is not None:  # проверка по имени User из списка юзеров
            if user.is_active:  # функция пайтона
                login(request, user)  # login - функция Пайтона
                return HttpResponse('Authenticated successfully')  # доступ получен
            else:
                return HttpResponse('Disabled account')  # аккаунт деактивирован
        else:  # имя user не найден в списках
            return HttpResponse('Invalid login')  # неверный логин

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


# Create your views here.
'''
POST - мы обрабатываем форму 
GET - мы создаем новую форму логина 
'''

'''
login() - user(Dima, 12345) - открывается сессия 
authenticate() - user(username, password) - просто вставляются значения, но сессия не открывается

'''
