# Django Working With Data
1. Django Admin
2. Forms
3. Django Model forms
4. Django Filters
5. permissions
6. Decorators

## Unique images
```python
def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")[-1]
    full_name = f"{name}.{ext}"
    # full_name = "%s.%s" % (name, ext)
    return os.path.join('employees', full_name)
```

## Unique image (Model class)
```python
profile = models.ImageField(upload_to=unique_img_name, null=True, default="employees/default.png")
```

## Order By
```python
employees = Employee.objects.all().ordered('salary')
```

## Filtering
```python
employees = Employee.objects.filter(name__isstartswith="la")
```

## Pagination 
```python
paginator = Paginator(employees, 20)
page_number = request.GET.get("page")
data = paginator.get_page(page_number)
return render(request, 'all_employees.html', {"employees": data})
```
