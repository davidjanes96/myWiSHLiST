from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account



@login_required(login_url="login")
def account_view(request):
    account = Account.objects.get()

    context = {
        'account': account
    }
    return render (request, 'account/account.html', context)


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Username or password is incorrect.')

    return render(request, 'account/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('home')