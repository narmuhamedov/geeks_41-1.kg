from django.shortcuts import render
from django.http import HttpResponse


def news_blog_view(request):
    if request.method == 'GET':
        return HttpResponse('ВАШ РЕБЕНОК В НАДЕЖНЫХ РУКАХ '
                            'Вы можете быть уверены в безопасности вашего ребенка, '
                            'поскольку наш коллектив состоит из большого числа сотрудников, '
                            'ответственных за создание всех условий для комфортного обучения. '
                            'а наш офис расположен в престижном бизнес-центре "Виктори", '
                            'что обеспечивая надежное и безопасное окружение для работы.')


def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse('Всем привет меня зовут Радомир я backend developer')


def geeks_view(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Привет GEEKS</h1>')
