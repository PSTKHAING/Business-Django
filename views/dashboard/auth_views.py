from django.shortcuts import render,redirect
from authentication.models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from django.contrib import messages
from django.conf import settings

def AdminLogin(request):
    if request.method == "GET":
        return render(request, 'dashboard/login.html')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserModel.objects.get(email = email)
            if check_password(password, user.password):
                login(request, user)
                messages.success(request, f"Welcome {user.get_full_name}")
                return redirect('/dashboard/')
            else:
                messages.error(request, "Email or Password is incorrect!")
                return redirect(settings.ADMIN_LOGIN_URL)
        except UserModel.DoesNotExist:
            messages.error(request, "Email or Password is incorrect!")
            return redirect(settings.ADMIN_LOGIN_URL)