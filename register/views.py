from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            newmail = form.cleaned_data['email']
            form.save()
            #get the new user info and set the group for this user to LibraryMember
            user = User.objects.get(username=uname)
            email = User.objects.get(email=newmail)
            normal_user = Group.objects.get(name='NormalUser')
            user.groups.add(normal_user)
            user.save()
            email.save()
            send_mail(
                "Thanks for Registering!",
                "Thanks for registering for The Finance Tracker!",
                "skerz4900@gmail.com",
                [newmail],
                fail_silently=False,
            )
            return redirect('login')

        return redirect('register')
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

