from django.shortcuts import render


def home(request):
    title = 'CodeFuryWebDevHome'
    return render(request, 'CodeFuryWebDev/home.html', context={'title': title,
                                                                'username': request.user})
