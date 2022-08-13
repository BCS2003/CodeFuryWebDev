from django.shortcuts import render, redirect
from .models import PostModel


def home(request):
    title = 'Posts'
    return render(request, 'posts/home.html', context={'title': title})


def creatPost(request):
    form = PostModel()
    title = 'Login'
    message = ''
    if request.method == 'POST':
        form = PostModel(request.POST)
        pass
        redirect('postsHome')
    return render(request, 'posts/post.html', context={'title': title,
                                                       'form': form,
                                                       'message': message})
