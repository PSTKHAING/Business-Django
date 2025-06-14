from django.shortcuts import render,redirect
from authentication.models import *
from user.models import *
from myadmin.models import *

def BusinessPage(request):
    business = BusinessModel.objects.all()
    context = {
        'business': business
    }
    return render(request, 'user/business_page.html', context)

def BusinessPageCreate(request):
    if request.method == "GET":
        countries = CountryModel.objects.all().order_by('-created_at')
        business_types = BusinessTypeModel.objects.all().order_by('-created_at')
        context = {
            'business_types': business_types,
            'countries': countries
        }
        return render(request, 'user/business_page_create.html', context)
    if request.method == "POST":
        business = BusinessModel.objects.create(
            name = request.POST.get('name'),
            type_id = request.POST.get('type'),
            owner_id = request.user.id,
            bio = request.POST.get('bio'),
            profile = request.FILES.get('profile'),
            background_profile = request.FILES.get('background_profile'),
            phone = request.POST.get('phone'),
            email = request.POST.get('email'),
            website = request.POST.get('website'),
            address = request.POST.get('address'),
            country_id = request.POST.get('country'),
        )
        business.owner.is_business = True
        business.owner.save()
        business.save()
        return redirect(f'/business/page/profile/{business.id}/')
    
def BusinessPageDetails(request,id):
    business = BusinessModel.objects.get(id=id)
    posts = BusinessPostModel.objects.filter(business=business).order_by('-created_at')
    context = {
        'business': business,
        'posts': posts
        }
    return render(request, 'user/business_page_details.html', context)

def BusinessPageProfile(request,id):
    business = BusinessModel.objects.get(id = id)
    posts = BusinessPostModel.objects.filter(business = business).order_by('-created_at')
    context = {
        "posts":posts
    }
    return render(request, 'user/business_page_profile.html', context)

def BusinessPageDashboard(request,id):
    context = {
        
    }
    return render(request, 'user/business_page_dashboard.html', context)

def BusinessPageYourPage(request,id):
    context = {
        
    }
    return render(request, 'user/business_page_your_page.html', context)

def BusinessPagePrivacy(request,id):
    context = {
        
    }
    return render(request, 'user/business_page_privacy.html', context)

def BusinessPageSetting(request,id):
    context = {
        
    }
    return render(request, 'user/business_page_setting.html', context)

def BusinessPageProfileUpdate(request,id):
    business = BusinessModel.objects.get(id = id)
    if request.method == "POST":
        if request.FILES.get('profile'):
            business.profile.delete()
            business.profile = request.FILES.get("profile")
        if request.FILES.get("background_profile"):
            business.background_profile.delete()
            business.background_profile = request.FILES.get("background_profile")
        business.phone = request.POST.get('phone')
        business.name = request.POST.get('name')
        business.email = request.POST.get('email')
        business.bio = request.POST.get('bio')
        business.save()
        return redirect(f'/business/page/setting/{business.id}/')