from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main_app.app_forms import EmployeeForm, LoginForm
from main_app.models import Employee


# Create your views here.
@login_required
@permission_required('main_app.add_employee', raise_exception=True)
def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Save successful")
            return redirect('home')
    else:
        form = EmployeeForm()

    return render(request, 'employee.html', {"form": form})


@login_required
@permission_required('main_app.view_employee', raise_exception=True)
def all_employees(request):
    employees = Employee.objects.all()
    # employees = Employee.objects.all().ordered('salary')
    # employees = Employee.objects.all().order_by('-salary')  # SELECT * From employees
    # employees = Employee.objects.filter(name__istartswith='la').order_by('-salary')
    # employees = Employee.objects.filter(Q(name__contains="la") | Q(salary__gt=70000))
    # employees = Employee.objects.filter(Q(name__contains="la") & Q(salary__gt=70000))
    today = datetime.today()
    day = today.day
    month = today.month
    # employees = Employee.objects.filter(Q(name__contains="la") & ~Q(salary__gt=70000))

    # employees = Employee.objects.filter(dob__day=day, dob__month=month)
    paginator = Paginator(employees, 40)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_employees.html', {"employees": data})


@login_required
def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)  # SELECT * From employees WHERE id=1
    return render(request, 'employee_details.html', {"employee": employee})


@login_required
@permission_required('main_app.delete_employee')
def employee_delete(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    employee.delete()
    messages.warning(request, "The employee has been deleted")
    return redirect('all')


@login_required
@permission_required('main_app.view_employee')
def search_employee(request):
    search_word = request.GET['search_word']
    employees = Employee.objects.filter(Q(name__icontains=search_word) | Q(email__icontains=search_word))
    # Elastic search - NoSQL database
    paginator = Paginator(employees, 40)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, 'all_employees.html', {"employees": data})


@login_required
@permission_required('main_app.change_employee')
def employee_update(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)  # SELECT * FROM employees where id=?
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Update Successful")
            return redirect('details', emp_id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "update.html", {"form": form})


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        messages.error(request, "Wrong username or password")
        return render(request, "login.html", {"form": form})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')