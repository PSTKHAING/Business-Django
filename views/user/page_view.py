from django.shortcuts import render,redirect
from authentication.models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from user.models import *
from myadmin.models import *

def Index(request):
    user = UserModel.objects.get(id =request.user.id)
    posts = PostModel.objects.filter(country =user.country).order_by('-created_at').prefetch_related('media')
    context = {
        'posts':posts
    }
    return render(request, 'user/index.html',context)

def Agreement(request):
    return render(request,'user/agreement.html')

@login_required(login_url= settings.LOGIN_URL)
def ProfilePost(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request,'user/profile_post.html',context)

def ProfileAbout(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_about.html',context)

def ProfileChat(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_chat.html',context)

def ProfileConnection(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_connection.html',context)

def ProfileUpdate(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_update.html',context)

def ProfileEvent(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_event.html',context)

def ProfileGroup(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_group.html',context)

def ProfileNotification(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_notification.html',context)

def ProfilePhoto(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_photo.html',context)

def ProfileVideo(request):
    user = request.user
    context = {
        'user': user,
        }
    return render(request,'user/profile_video.html',context)