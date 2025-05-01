from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department, Role
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    employees = Employee.objects.all()
    return render(request, 'view_all_employee.html', {'employees': employees})

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department_id = request.POST['department']
        role_id = request.POST['role']
        salary = request.POST['salary']
        phone = request.POST['phone']
        hire_date = request.POST['hire_date']

        department = Department.objects.get(id=department_id)
        role = Role.objects.get(id=role_id)

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            department=department,
            role=role,
            salary=salary,
            phone=phone,
            hire_date=hire_date
        )
        return redirect('all_emp')

    departments = Department.objects.all()
    roles = Role.objects.all()
    return render(request, 'add_employee.html', {'departments': departments, 'roles': roles})

def remove_emp(request, emp_id):
    # Fetch the employee by ID or return a 404 if not found
    employee = get_object_or_404(Employee, id=emp_id)
    
    # Delete the employee
    employee.delete()
    
    # Redirect to the "Remove Employee" page
    return redirect('remove_emp_page')


def filter_emp(request):
    # Fetch all employees, departments, and roles
    employees = Employee.objects.all()
    departments = Department.objects.all()
    roles = Role.objects.all()

    # Apply filters based on GET parameters
    name = request.GET.get('name', '')
    department = request.GET.get('department', '')
    role = request.GET.get('role', '')

    if name:
        employees = employees.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
    if department:
        employees = employees.filter(department__name=department)
    if role:
        employees = employees.filter(role__name=role)

    # Pass employees, departments, and roles to the template
    return render(request, 'filter_employee.html', {
        'employees': employees,
        'departments': departments,
        'roles': roles,
    })


def remove_emp_page(request):
    # Fetch all employees from the database
    employees = Employee.objects.all()
    return render(request, 'remove_employee.html', {'employees': employees})