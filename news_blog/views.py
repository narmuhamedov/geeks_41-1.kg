from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from news_blog.models import Employees, Poster, Product
from . import forms


# CRUD CREATE-READ-UPDATE-DELETE

# Редактирование сотрудника

def edit_employee_view(request, id):
    emp_id = get_object_or_404(Employees, id=id)
    if request.method == 'POST':
        form = forms.EmpForm(request.POST, instance=emp_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Employee successfully updated!</h3>'
                                '<a href="/employees/">На список сотрудников</a>')
    else:
        form = forms.EmpForm(instance=emp_id)
    return render(request, template_name='blog/edit_employee.html',
                  context={
                      'form': form,
                      'emp_id': emp_id
                  })


# Удаление сотрудника
def drop_employee_view(request, id):
    emp_id = get_object_or_404(Employees, id=id)
    emp_id.delete()
    return HttpResponse('Employee deleted <a href="/employees/">На список сотрудников</a>')


# Добавление сотрудника

def create_employee_view(request):
    if request.method == "POST":
        form = forms.EmpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Employee successfully created!</h3>'
                                '<a href="/employees/">На список сотрудников</a>')
    else:
        form = forms.EmpForm()

    return render(request, template_name='blog/create_employee.html',
                  context={'form': form})


# Функция для отображения не полной информации
def employees_list_view(request):
    if request.method == 'GET':
        query = Employees.objects.filter().order_by('-id')
        posters = Poster.objects.filter().order_by('-id')
        return render(
            request,
            template_name='blog/employees_list.html',
            context={
                'employees': query,
                'posters': posters
            }
        )


# Функция для полного отображения данных сотрудника (id)
def employees_detail_view(request, id):
    if request.method == 'GET':
        employee_id = get_object_or_404(Employees, id=id)
        return render(
            request,
            template_name='blog/employees_detail.html',
            context={
                'emp_id': employee_id
            }
        )


########## Многие ко многим ################

def all_products(request):
    if request.method == 'GET':
        products = Product.objects.filter().order_by('-id')
        return render(request, template_name='products/all_products.html',
                      context={'products': products})


def for_eat_view(request):
    if request.method == 'GET':
        eat_food = Product.objects.filter(tags__name='Еда').order_by('-id')
        return render(request, template_name='products/for_eat_view.html',
                      context={
                          'eat_food': eat_food
                      })


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
