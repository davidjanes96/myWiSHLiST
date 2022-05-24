from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Account
from .forms import CustomUserCreationForm



@login_required(login_url="login")
def account_view(request):
    account = Account.objects.get()

    context = {
        'account': account
    }
    return render (request, 'account/account.html', context)


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'Registered successfully!')

            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'An error has occured during registration.')

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'account/login_register.html', context)



def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect.')

    return render(request, 'account/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'Successfully logged out.')
    return redirect('home')


