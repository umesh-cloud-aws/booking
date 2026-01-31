from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html')
def book_appointment(request):
    return render(request, 'book_appointment.html')
def services(request):
    return render(request, 'services.html')
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')
def contact(request):
    return render(request, 'contact.html')