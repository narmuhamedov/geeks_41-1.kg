from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from news_blog.models import Employees, Poster, Product
from django.views import generic
from . import forms


# Кнопка поиска
class SearchListView(generic.ListView):
    template_name = "blog/employees_list.html"
    context_object_name = 'employees'
    paginate_by = 5

    def get_queryset(self):
        return Employees.objects.filter(name__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context





# CRUD CREATE-READ-UPDATE-DELETE

# Редактирование сотрудника
class EditEmployeeView(generic.UpdateView):
    template_name = 'blog/edit_employee.html'
    form_class = forms.EmpForm
    success_url = '/employees/'

    def get_object(self, **kwargs):
        emp_id = self.kwargs.get('id')
        return get_object_or_404(Employees, id=emp_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditEmployeeView, self).form_valid(form=form)


# def edit_employee_view(request, id):
#     emp_id = get_object_or_404(Employees, id=id)
#     if request.method == 'POST':
#         form = forms.EmpForm(request.POST, instance=emp_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Employee successfully updated!</h3>'
#                                 '<a href="/employees/">На список сотрудников</a>')
#     else:
#         form = forms.EmpForm(instance=emp_id)
#     return render(request, template_name='blog/edit_employee.html',
#                   context={
#                       'form': form,
#                       'emp_id': emp_id
#                   })


# Удаление сотрудника
class EmployeeDeleteView(generic.DeleteView):
    template_name = 'blog/confirm_delete.html'
    success_url = '/employees/'

    def get_object(self, **kwargs):
        emp_id = self.kwargs.get('id')
        return get_object_or_404(Employees, id=emp_id)


# def drop_employee_view(request, id):
#     emp_id = get_object_or_404(Employees, id=id)
#     emp_id.delete()
#     return HttpResponse('Employee deleted <a href="/employees/">На список сотрудников</a>')


# Добавление сотрудника

class CreateEmployeeView(generic.CreateView):
    template_name = 'blog/create_employee.html'
    form_class = forms.EmpForm
    success_url = '/employees/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateEmployeeView, self).form_valid(form=form)


# def create_employee_view(request):
#     if request.method == "POST":
#         form = forms.EmpForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Employee successfully created!</h3>'
#                                 '<a href="/employees/">На список сотрудников</a>')
#     else:
#         form = forms.EmpForm()
#
#     return render(request, template_name='blog/create_employee.html',
#                   context={'form': form})


# Функция для полного отображения данных сотрудника (id)
class EmployeesDetailView(generic.DetailView):
    template_name = 'blog/employees_detail.html'
    context_object_name = 'emp_id'

    def get_object(self, **kwargs):
        emp_id = self.kwargs.get('id')
        return get_object_or_404(Employees, id=emp_id)


# def employees_detail_view(request, id):
#     if request.method == 'GET':
#         employee_id = get_object_or_404(Employees, id=id)
#         return render(
#             request,
#             template_name='blog/employees_detail.html',
#             context={
#                 'emp_id': employee_id
#             }
#         )


# Функция для отображения не полной информации

class EmployeesListView(generic.ListView):
    template_name = "blog/employees_list.html"
    context_object_name = "employees"
    model = Employees
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posters'] = Poster.objects.order_by('-id')
        return context


# def employees_list_view(request):
#     if request.method == 'GET':
#         query = Employees.objects.filter().order_by('-id')
#         posters = Poster.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='blog/employees_list.html',
#             context={
#                 'employees': query,
#                 'posters': posters
#             }
#         )


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
