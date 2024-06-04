from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employees_list_view),
    path('employees/<int:id>/', views.employees_detail_view),

    path('news_blog/', views.news_blog_view),
    path('about_me/', views.about_me_view),
    path('geeks/', views.geeks_view),
]
