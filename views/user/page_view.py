from django.shortcuts import render,redirect
from authentication.models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from user.models import *
from myadmin.models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def Index(request):
    posts = []
    selectcountry = ""
    try:
        user = UserModel.objects.get(id =request.user.id)
        posts = PostModel.objects.filter(country =user.country).order_by('-created_at').prefetch_related('media')
        selectcountry = request.POST.get('country')
        
        if selectcountry:
            request.session['country'] = selectcountry
            posts = PostModel.objects.filter(country = selectcountry).order_by('-created_at').prefetch_related('media')
        else:
            request.session['country'] = user.country.id
    except:
        user = None
        posts = PostModel.objects.all().order_by('-created_at').prefetch_related('media')
    countries = CountryModel.objects.all()
    context = {
        'posts':posts,
        'countries':countries,
        'selectcountry':selectcountry
    }
    return render(request, 'user/index.html',context)

def Search(request):
    country = request.session['country']
    search = request.GET.get('search')
    posts = PostModel.objects.filter(country = country,content__contains=search).order_by('-created_at').prefetch_related('media')
    countries = CountryModel.objects.all()
    context = {
        'posts':posts,
        'countries':countries,
        'selectcountry':country
    }
    return render(request, 'user/index.html',context)

def Agreement(request):
    return render(request,'user/agreement.html')

@login_required(login_url= settings.LOGIN_URL)
def ProfilePost(request,id):
    
    context = {
        
    }
    return render(request,'user/profile_post.html',context)

def ProfileAbout(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_about.html',context)

def ProfileChat(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_chat.html',context)

def ProfileConnection(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_connection.html',context)

def ProfileUpdate(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_update.html',context)

def ProfileEvent(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_event.html',context)

def ProfileGroup(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_group.html',context)

def ProfileNotification(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_notification.html',context)

def ProfilePhoto(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_photo.html',context)

def ProfileVideo(request,id):
    
    context = {
        
        }
    return render(request,'user/profile_video.html',context)