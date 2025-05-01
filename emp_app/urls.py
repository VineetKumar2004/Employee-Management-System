from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('all_emp/', views.all_emp, name='all_emp'),  # View all employees
    path('add_emp/', views.add_emp, name='add_emp'),  # Add an employee
    path('remove_emp/', views.remove_emp_page, name='remove_emp_page'),
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp'),
    path('filter_emp/', views.filter_emp, name='filter_emp'),  # Filter employees
]