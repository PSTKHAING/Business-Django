from django.shortcuts import render,redirect
from authentication.models import *
from user.models import *
from myadmin.models import *

def BusinessPage(request):
    business = BusinessModel.objects.all()
    my_business_page = BusinessModel.objects.get(owner_id = request.user.id)
    context = {
        'business': business,
        'my_business_page':my_business_page.id
    }
    return render(request, 'user/business_page.html', context)

def BusinessPageCreate(request):
    if request.method == "GET":
        business_types = BusinessTypeModel.objects.all().order_by('-created_at')
        context = {
            'business_types': business_types,
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
        )
        business.save()
        return redirect('/business/page/info/')
    
def BusinessPageInfo(request):
    business = BusinessModel.objects.get(owner_id =request.user.id)
    countries = CountryModel.objects.all().order_by('-created_at')
    business_types = BusinessTypeModel.objects.all().order_by('-created_at')
    if request.method == "GET":
        context = {
            'business': business,
            'business_types': business_types,
            'countries': countries,
        }
        return render(request,'user/business_page_info.html',context)
    if request.method == "POST":
        business.type_id = request.POST.get('type')
        business.phone = request.POST.get('phone')
        business.website = request.POST.get('website')
        business.address = request.POST.get('address')
        business.country_id = request.POST.get('country')
        business.save()
        return redirect('/business/page/profile/')

def BusinessPageProfile(request,id):
    business = BusinessModel.objects.get(id = id)
    context = {
        'business': business,
    }
    return render(request, 'user/business_page_profile.html', context)

def BusinessPageDashboard(request):
    business = BusinessModel.objects.get(owner_id=request.user.id)
    context = {
        'business': business,
    }
    return render(request, 'user/business_page_dashboard.html', context)

def BusinessPageYourPage(request):
    business = BusinessModel.objects.get(owner_id=request.user.id)
    context = {
        'business': business,
    }
    return render(request, 'user/business_page_your_page.html', context)

def BusinessPagePrivacy(request):
    business = BusinessModel.objects.get(owner_id=request.user.id)
    context = {
        'business': business,
    }
    return render(request, 'user/business_page_privacy.html', context)

def BusinessPageSetting(request):
    business = BusinessModel.objects.get(owner_id=request.user.id)
    context = {
        'business': business,
    }
    return render(request, 'user/business_page_setting.html', context)

def BusinessPageProfileUpdate(request):
    business = BusinessModel.objects.get(owner_id=request.user.id)
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
        return redirect('/business/page/setting/')