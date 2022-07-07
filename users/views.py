from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request , 'Logged in successfully..')
            return redirect('/online_judge')
        else:
            messages.info(request , 'The username or password is incorrect..')
            return redirect('/auth/login_user')
    else:
        return render(request, 'auth/login.html' , {})

def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is created, you can login now..')
            return redirect('/auth/login_user')


    context = { 'form' : form }
    return render(request, 'auth/register.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out..')
    return redirect("/online_judge")
