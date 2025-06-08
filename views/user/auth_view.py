from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from authentication.models import *
from django.contrib import messages
from django.contrib.auth import login,logout
from django.conf import settings
from user.models import *
from myadmin.models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime

def generate_random_code():
    from random import randrange 
    random_code = randrange(100000, 999999) 
    return random_code

def LogIn(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'user/login.html')

    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserModel.objects.get(email=email)
            if check_password(password, user.password):
                login(request, user)
                messages.success(request, f"Welcome {user.username}")
                return redirect('/')
            else:
                messages.error(request, "Password is incorrect!")
                return redirect('/login/')
        
        except UserModel.DoesNotExist:
            messages.error(request, "User not found")
            return redirect('/login/')

def Register(request):
    if request.method == "GET":
        countries = CountryModel.objects.all().order_by('-created_at')
        context = {
            "countries" : countries
        }
        return render(request, 'user/register.html',context)

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")  # Avoid using `email` to prevent conflicts

        if UserModel.objects.filter(email=email).exists():
            messages.error(request, "Email has been already used!")
            return redirect('/login/')

        password = request.POST.get('password')
        user = UserModel.objects.create_user(
            username=username,
            email=email,
            country_id = request.POST.get('country'),
            password=password,
        )
        user.save()

        otp_code = generate_random_code()  # Ensure this returns a string
        otp = OTPModel.objects.create(
            user=user,
            code=otp_code
        )
        otp.save()

        # Render HTML email template
        html_content = render_to_string("user/emails/otp_email.html", {"user": user, "otp": otp_code})
        text_content = strip_tags(html_content)

        # Send email (renamed variable to `email_message`)
        email_message = EmailMultiAlternatives(
            subject=f'Welcome {user.username}, Your OTP code is {otp_code}',
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],  
        )
        email_message.attach_alternative(html_content, "text/html")
        email_message.send()

        return redirect('/otp/' + user.email + '/')
    
def OTP(request, email):
    if request.method == "GET":
        user = UserModel.objects.filter(email=email).first()
        if user:
            return render(request, "user/otp.html", {"email": email})
        else:
            messages.error(request, "User not found")
            return redirect('/login/')
    
    if request.method == "POST":
        try:
            user = UserModel.objects.get(email=email)
            code = request.POST.get('code')

            otp_entry = OTPModel.objects.filter(user=user).latest('created_at')
            otp_code = otp_entry.code

            time_diff = timezone.now() - otp_entry.created_at
            if time_diff.total_seconds() > 300:
                otp_entry.delete()
                messages.error(request, "OTP has expired, please request a new one.")
                return redirect('/otp/' + email + '/')

            entered_code = code.strip()

            if entered_code == str(otp_code):
                user.is_active = True
                user.save()
                login(request,user)
                otp_entry.delete()
                messages.success(request, "OTP verified successfully!")
                return redirect('/agreement/')
            else:
                messages.error(request, "OTP does not match!")
                return redirect('/otp/' + email + '/')
        except UserModel.DoesNotExist:
            messages.error(request, "User not found")
            return redirect('/login/')
        except OTPModel.DoesNotExist:
            messages.error(request, "OTP not found or expired")
            return redirect('/otp/' + email + '/')

def ResendOTP(request, email):
    if request.method == "GET":
        try:
            user = UserModel.objects.get(email=email)
            OTPModel.objects.filter(user=user).delete()
            otp_code = generate_random_code()
            otp = OTPModel.objects.create(
                user=user,
                code= otp_code
            )
            otp.save()
            # Render HTML email template
            html_content = render_to_string("user/emails/otp_email.html", {"user": user, "otp": otp_code})
            text_content = strip_tags(html_content)

            # Send email (renamed variable to `email_message`)
            email_message = EmailMultiAlternatives(
                subject=f'Welcome {user.username}, Your OTP code is {otp_code}',
                body=text_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email],  
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()
            messages.success(request, "New OTP has been sent to your email.")
            return redirect('/otp/' + user.email + '/')
        except UserModel.DoesNotExist:
            messages.error(request, "User not found")
            return redirect('/login/')
    
def LogOut(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

def ConfirmEmailToResetPassword(request):
    if request.method == "GET":
        return render(request,"user/confirm_email_to_reset_password.html")
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            messages.error(request, "Email not found.")
            return redirect('/confirm_email_to_reset_password/')
        if UserModel.objects.filter(email = email).exists():
            reset_link = user.reset_password_link
            html_content = render_to_string("user/emails/email_confirmation.html", {"user": user,"reset_link": reset_link})
            text_content = strip_tags(html_content)

            email_message = EmailMultiAlternatives(
                subject='Email Confirmation',
                body=text_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()
            messages.success(request, "Reset password link sent to your email.")
            return redirect('/confirm_email_to_reset_password/')
        else:
            messages.error(request,"Email does not found!")
            return redirect('/confirm_email_to_reset_password/')
        
def ResetPassword(request,email,reset_id):
    if request.method == "GET":
        user = UserModel.objects.get(email=email, id =reset_id)
        context = {
            "user":user
        }
        return render(request,"user/reset_password.html",context)
    if request.method == "POST":
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                messages.error(request,"Email does not found!")
                return redirect(f'/reset_password/{email}/{reset_id}/')
            if user.id == reset_id:
                user.set_password(password)
                user.save()
                messages.success(request,"Password reset successfully!")
                return redirect('/login/')
            else:
                messages.error(request,"Invalid reset id!")
                return redirect(f'/reset_password/{email}/{reset_id}/')
        else:
            messages.error(request,"Password and confirm password does not match!")
            return redirect(f'/reset_password/{email}/{reset_id}/')