from django.urls import path
from . import views

urlpatterns = [

    path('all_products/', views.all_products),
    path('eat_products/', views.for_eat_view),


    path('employees/', views.EmployeesListView.as_view()),
    path('employees/<int:id>/', views.EmployeesDetailView.as_view()),
    path('employees/<int:id>/delete/', views.EmployeeDeleteView.as_view()),
    path('employees/<int:id>/update/', views.EditEmployeeView.as_view()),
    path('create_employee/', views.CreateEmployeeView.as_view()),
    path('search/', views.SearchListView.as_view(), name='search'),


    path('news_blog/', views.news_blog_view),
    path('about_me/', views.about_me_view),
    path('geeks/', views.geeks_view),
]
