from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from allauth.account.forms import SignupForm
from django.contrib import messages
from devs.forms import AddDevForm
from devs.models import Dev


def index(request):
    context = dict()

    return render(request, "devs/index.html", context)


def login(request):
    context = dict()
    context["form"] = AddDevForm()

    return render(request, "devs/login.html", context)


@csrf_exempt
def create_dev(request):
    form = AddDevForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Account created successfully.")
    else:
        messages.error(request, "Whoops! Something went wrong.")
    return redirect("login")
