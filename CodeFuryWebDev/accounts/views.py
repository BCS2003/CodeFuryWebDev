from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import CustomUserCreationForm, LoginForm


def home(request):
    title = "Accounts"
    return render(request, 'accounts/home.html', context={'title': title})


def loginPage(request):
    form = LoginForm()
    message = ''
    title = 'Login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('codeFuryWebDevHome')
            message = 'Login failed!'
    return render(request, 'accounts/login.html', context={'title': title,
                                                           'form': form,
                                                           'message': message})


def logoutPage(request):
    logout(request)
    return redirect('codeFuryWebDevHome')


def signupPage(request):
    form = CustomUserCreationForm()
    message = ''
    title = 'Login'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('codeFuryWebDevHome')
        else:
            message = 'something went wrong, try again'
    return render(request, 'accounts/signup.html', context={'title': title,
                                                            'form': form,
                                                            'message': message})
