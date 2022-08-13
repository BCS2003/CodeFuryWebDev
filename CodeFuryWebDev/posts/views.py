from django.shortcuts import render, redirect
from .forms import PostCreationForm
from .models import PostModel


def home(request):
    title = 'Posts'
    posts = PostModel.objects.all()[:25]
    return render(request, 'posts/home.html', context={'title': title, 'posts': posts})


def creatPost(request):
    form = PostCreationForm()
    title = 'Login'
    message = ''
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form_c = form.cleaned_data
            founders = form_c.pop('founders')
            pm = PostModel.objects.create(**form_c)
            pm.founders.add(founders.id)
        return redirect('postsHome')
    return render(request, 'posts/post.html', context={'title': title,
                                                       'form': form,
                                                       'message': message})
