from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

        else:
            context = {'message' : 'Entered wrong username or password.' }
            return render(request, 'accounts/user_login.html', context)

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'accounts/user_login.html')



def user_signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print('In')
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/user_signup.html', {'message' : 'Somthing went wrong!!'})

    if request.method == 'GET':
        context = {'form' : form}
        return render(request, 'accounts/user_signup.html', context )


def user_logout(request):
    logout(request)
    return redirect('login')