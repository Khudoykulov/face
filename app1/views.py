from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('app1:home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('app1:login')  # Replace 'login' with your desired redirect URL
    else:
        return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('app1:login')  # Replace 'login' with your desired redirect URL