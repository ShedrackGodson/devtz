from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from devs.forms import AddCertificateForm, AddOtherExperienceForm
from social_django.models import UserSocialAuth
from django.shortcuts import redirect, render
from devs.models import Availability, Dev, DevCertificates, EmailPreference, OtherExperience, PublicPreference, SkillSet
from django.contrib import messages


def index(request):
    context = dict()

    return render(request, "devs/index.html", context)


@login_required
def settings(request):
    user = request.user

    return render(request, 'devs/settings.html', {
        'user': user,

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


@login_required
@csrf_exempt
def delete_account(request, dev_id):
    if request.method == "POST":
        Dev.objects.get(id=dev_id).delete()
        messages.success(request, "Account deleted successfully.")
    return redirect("home")  # Redirect to the blog page


@login_required
def social_auths(request):
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
    return render(request, "devs/settings.html", {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def preferences(request):

    return render(request, "devs/settings.html", {

    })


@login_required
def save_dev_preference(request, dev_id):
    dev = PublicPreference.objects.get(
        dev__id=dev_id
    )
    both_emails = request.POST.get("emails")
    hireable = request.POST.get("hireable")
    bio = request.POST.get("bio")
    phone = request.POST.get("phone")
    gender = request.POST.get("gender")
    if both_emails:
        dev.both_emails = True
    else:
        dev.both_emails = False
    if hireable:
        dev.hireable = True
    else:
        dev.hireable = False
    if bio:
        dev.bio = True
    else:
        dev.bio = False
    if phone:
        dev.phone = True
    else:
        dev.phone = False
    if gender:
        dev.gender = True
    else:
        dev.gender = False
    dev.save()
    messages.success(request, "Changes saved.",
                     fail_silently=False)
    return HttpResponseRedirect(
        request.META.get("HTTP_REFERER")
    )


@login_required
def email_notifications(request):

    return render(request, "devs/settings.html", {

    })


@login_required
def save_email_preference(request, dev_id):
    dev = EmailPreference.objects.get(
        dev__id=dev_id
    )
    logins = request.POST.get("logins")
    message = request.POST.get("messages")
    updates = request.POST.get("updates")

    if logins:
        dev.logins = True
    else:
        dev.logins = False
    if message:
        dev.messages = True
    else:
        dev.messages = False
    if updates:
        dev.updates = True
    else:
        dev.updates = False
    dev.save()
    messages.success(request, "Changes saved.",
                     fail_silently=False)
    return HttpResponseRedirect(
        request.META.get("HTTP_REFERER")
    )


@login_required
def stacks(request):

    return render(request, "devs/settings.html", {

    })


@login_required
def profile(request, username):
    context = dict()
    context["skill_sets"] = SkillSet.objects.all()
    context["form"] = AddOtherExperienceForm()
    context["certificate_form"] = AddCertificateForm()
    context["availabilities"] = {
        "more": "More than 30 hrs/week",
        "less": "Less than 30 hrs/week",
        "open": "As needed - open to offers",
        "not": "Not Available"
    }

    return render(request, "devs/profile.html", context)


@login_required
@csrf_exempt
def add_other_experience(request, username):
    if request.method == "POST":
        form = AddOtherExperienceForm(request.POST)
        try:
            dev = Dev.objects.get(username=username)
            if form.is_valid():
                form.save(commit=False, dev=dev)
                form.save(commit=True, dev=dev)
                messages.success(request, "Experience added.")
            else:
                messages.error(request, "Something went wrong.")
                # print(form.errors)
        except Exception as e:
            # print(e)
            messages.error(request, "Something went wrong.")
        return redirect("profile", dev.username)


@login_required
@csrf_exempt
def delete_other_experience(request, experience_id, dev_username):
    try:
        dev = Dev.objects.get(username=dev_username)
        experience = OtherExperience.objects.get(
                id=experience_id
            )
        if dev == request.user and experience.dev == request.user:
            experience.delete()
            messages.success(request, "Experience deleted.")
    except:
        messages.error(request, "Something went wrong.")
    return redirect("profile", dev.username)


@login_required
@csrf_exempt
def update_other_experience(request, experience_id, dev_username):
    try:
        dev = Dev.objects.get(username=dev_username)
        experience = OtherExperience.objects.get(
                id=experience_id
            )
        if dev == request.user and experience.dev == request.user:
            experience.subject = request.POST.get("subject")
            experience.description = request.POST.get("description")
            experience.save()
            messages.success(request, "Experience updated.")
    except:
        messages.error(request, "Something went wrong.")
    return redirect("profile", dev.username)


@login_required
@csrf_exempt
def add_certificate(request, username):
    if request.method == "POST":
        try:
            DevCertificates.objects.create(
                dev=Dev.objects.get(username=username),
                certificate_name=request.POST.get("certificate_name"),
                provider=request.POST.get("provider"),
                description=request.POST.get("description"),
                issue_date=request.POST.get("issue_date"),
                expiration=request.POST.get("expiration"),
                certificate_id=request.POST.get("certificate_id"),
                certificate_url=request.POST.get("certificate_url")
            )
            messages.success(request, "Certificate added.")
        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong.")
        return redirect("profile", username)


@login_required
@csrf_exempt
def save_availability(request, dev_username):
    try:
        object = Availability.objects.get(
            dev__username=dev_username
        )
        availability = request.POST.get("availability")
        object.days_available = availability
        if availability == "not":
            object.available = False
        else:
            object.available = True
        object.save()
        messages.success(request, "Status changed.")
    except Availability.DoesNotExist:
        pass
    return redirect("profile", dev_username)

