from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    data = {'title': 'Главная страница '}
    return render(request, 'mainpage/index.html', data)

def about(request):
    data = {'title': 'Информация о разработчике'}
    return render(request, 'mainpage/about.html', data)

