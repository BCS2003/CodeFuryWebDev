from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import CustomUserCreationForm, LoginForm


def accountsHome(request):
    return HttpResponse("<h1>Accounts</h1>")


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
                return redirect('projectRoadMapHome')
            message = 'Login failed!'
    return render(request, 'accounts/login.html', context={'title': title,
                                                           'form': form,
                                                           'message': message})


def logoutPage(request):
    logout(request)
    return redirect('projectRoadMapHome')


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

            return redirect('projectRoadMapHome')
        else:
            message = 'something went wrong, try again'
    return render(request, 'accounts/signup.html', context={'title': title,
                                                            'form': form,
                                                            'message': message})
