from django.shortcuts import render


def codeFuryWebDevHome(request):
    title = 'CodeFuryWebDevHome'
    return render(request, 'CodeFuryWebDev/home.html', context={'title': title,
                                                                'username': request.user})
