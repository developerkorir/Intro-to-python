from django.shortcuts import render


# Create your views here.
def home_page(request):
    name = "Calton Korir"
    age = 18

    data = {
        "name": name,
        "age": age
    }
    return render(request, 'index.html', context=data)
