from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from crm.forms import OrderForm
from crm.models import Order
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from cms.models import CmsSlider


@login_required
def dashboard(request):
    form = OrderForm()
    slider_list = CmsSlider.objects.all()
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard', 'form': form, 'slider_list': slider_list})  # это у нас всё декортатор


# у нас как только мы входим на наш рабочий стол сайта, он проверяется на то, аутентифирован ли пользователь


def thanks_page(request):
    name_surname = request.POST['name_surname']
    age = request.POST['age']
    location = request.POST['location']
    element = Order(order_name_surname=name_surname, order_age=age, order_location=location)
    element.save()
    return render(request, './thanks_page.html')


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
