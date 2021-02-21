from django.shortcuts import render


def index(request):
    context = dict()

    return render(request, "devs/index.html", context)


def login(request):
    context = dict()

    return render(request, "devs/login.html", context)
