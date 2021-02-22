from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from social_django.models import UserSocialAuth
from django.shortcuts import redirect, render
from django.contrib import messages
from devs.models import Dev


def index(request):
    context = dict()

    return render(request, "devs/index.html", context)


@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() >
                      1 or user.has_usable_password())

    return render(request, 'devs/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'devs/password.html', {'form': form})


@login_required
def change_password(request, dev_id):
    dev = Dev.objects.get(id=dev_id)
    current_password = request.POST.get("current_password")
    new_password = request.POST.get("new_password")
    new_password2 = request.POST.get("new_password2")
    try:
        status = authenticate(request, username=dev.username,
                              password=current_password)
        if status:
            if new_password == new_password2:
                dev.set_password(new_password)
                dev.save()
                messages.success(request, "Password successfully changed.")
            else:
                messages.error(request, "Passwords not matching.")
        else:
            messages.error(request, "Invalid credentials.")
    except Exception as e:
        print(e)
    return redirect("settings")
