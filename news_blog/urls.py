from django.urls import path
from . import views

urlpatterns = [

    path('all_products/', views.all_products),
    path('eat_products/', views.for_eat_view),


    path('employees/', views.employees_list_view),
    path('employees/<int:id>/', views.employees_detail_view),
    path('employees/<int:id>/delete/', views.drop_employee_view),
    path('employees/<int:id>/update/', views.edit_employee_view),
    path('create_employee/', views.create_employee_view),


    path('news_blog/', views.news_blog_view),
    path('about_me/', views.about_me_view),
    path('geeks/', views.geeks_view),
]
