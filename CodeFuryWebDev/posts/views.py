from django.shortcuts import render, redirect
from .forms import PostCreationForm


def home(request):
    title = 'Posts'
    return render(request, 'posts/home.html', context={'title': title})


def creatPost(request):
    form = PostCreationForm()
    title = 'Login'
    message = ''
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        redirect('postsHome')
    return render(request, 'posts/post.html', context={'title': title,
                                                       'form': form,
                                                       'message': message})
