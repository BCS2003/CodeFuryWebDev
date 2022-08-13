from django.shortcuts import render


def home(request):
    title = 'Chats'
    return render(request, 'chats/home.html', context={'title': title})
