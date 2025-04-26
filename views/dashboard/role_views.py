from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login,logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from authentication.decorators import role_permission_required
from django.contrib.auth.models import Permission
from authentication.models import *
import openpyxl
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
import urllib.parse
from datetime import datetime
from django.db import IntegrityError

@login_required(login_url=settings.LOGIN_URL)
# @role_permission_required('authentication.view_rolemodel')
def RoleList(request):
    roles = RoleModel.objects.all().order_by('-created_at')
    permissions = Permission.objects.all()
    context = {
        'roles': roles,
        'permissions': permissions
    }
    return render(request,'dashboard/role_list.html',context)

@login_required(login_url=settings.LOGIN_URL)
# @role_permission_required('authentication.add_rolemodel')
def RoleCreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if RoleModel.objects.filter(name=name).exists():
            messages.error(request, "Role Name has already been used!")
            return redirect('/role/list/')
        
        selected_permissions = request.POST.getlist('permissions')
        if not selected_permissions:
            messages.warning(request, "Please select at least one permission.")
            return redirect('/role/list/')
        
        role = RoleModel.objects.create(name=name)
        role.permissions.set(selected_permissions)
        role.save()
        
        messages.success(request, "Role created successfully.")
        return redirect('/role/list/')  

@login_required(login_url=settings.LOGIN_URL)
# @role_permission_required('authentication.change_rolemodel')
def RoleUpdate(request,pk):
    role = RoleModel.objects.get(id =pk)
    if request.method == 'POST':
        new = request.POST.get('name')
        selected_permissions = request.POST.getlist('permissions')

        current_permissions = set(role.permissions.values_list('id', flat=True))
        new_permissions = set(map(int, selected_permissions))

        if role.name == new and current_permissions == new_permissions:
            messages.warning(request, 'No changes were made.')
            return redirect('/role/list/')

        role.name = new
        role.permissions.set(new_permissions)
        role.save()

        messages.success(request, 'Role updated successfully.')
        return redirect('/role/list/')

@login_required(login_url=settings.LOGIN_URL)
# @role_permission_required('authentication.delete_rolemodel')
def RoleDelete(request,pk):
    role = RoleModel.objects.get(id =pk)
    role.delete()
    messages.success(request, "Role deleted successfully.")
    return redirect('/role/list/')
