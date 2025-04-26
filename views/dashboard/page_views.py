from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url=settings.LOGIN_URL)
def Dashboard(request):
    return render(request, 'dashboard/dashboard.html')