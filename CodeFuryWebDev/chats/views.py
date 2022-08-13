from django.shortcuts import render
from .models import Message


def home(request):
    title = 'Chats'
    return render(request, 'chats/home.html', context={'title': title})


def room(request):
    username = request.user
    roomname = request.GET.get('room', None)
    msg = request.GET.get('msg', None)
    if msg is None:
        messages = Message.objects.filter(room=roomname)[0:25]
        return render(request, 'chats/room.html',
                      context={'roomname': roomname, 'username': username, 'messages': messages})
    else:
        Message.objects.create(username=username, room=roomname, content=msg)
        messages = Message.objects.filter(room=roomname)[0:25]
        return render(request, 'chats/room.html',
                      context={'roomname': roomname, 'username': username, 'messages': messages})
