from django.shortcuts import render,redirect
from user.models import *
from django.contrib import messages
from django.http import JsonResponse
import json

def PostCreate(request):
    if request.method == 'GET':
        context = {
            
        }
        return render(request, 'user/post_create.html', context)
    if request.method == 'POST':
        content = request.POST.get('content', '')
        
        files = request.FILES.getlist('media')

        user = UserModel.objects.get(id =request.user.id)

        post = PostModel.objects.create(
            author=user,
            content=content,
            country = user.country
        )
        
        for file in files:
            file_type = 'file'
            if file.content_type.startswith('image'):
                file_type = 'image'
            elif file.content_type.startswith('video'):
                file_type = 'video'

            media = PostMediaModel.objects.create(
                post=post,
                file=file,
                file_type=file_type
            )
            media.save()

        messages.success(request, "Post created successfully!")
        return redirect('/')