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
    
def PostDetails(request,id):
    post = PostModel.objects.get(id=id)
    comments = CommentModel.objects.filter(post=post).order_by('-created_at')
    context = {
        'post': post,
        'comments': comments,
        }
    return render(request, 'user/post_details.html', context)

def PostComment(request,id,page):
    post = PostModel.objects.get(id=id)
    if request.method == 'POST':
        comment = CommentModel.objects.create(
            user =request.user,
            post = post,
            content = request.POST.get('content')
        )
        comment.save() 
        return redirect(f'/post/detail/{id}/') if page == "details" else redirect('/')

def PostReaction(request, id):
    post = PostModel.objects.get(id=id)
    if request.user in post.reaction.all():
        post.reaction.remove(request.user)
        message = 'Like removed'
    else:
        post.reaction.add(request.user)
        message = 'Like added'
    return JsonResponse({'message': message})