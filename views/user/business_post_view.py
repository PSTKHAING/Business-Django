from django.shortcuts import render,redirect
from user.models import *
from django.contrib import messages
from django.http import JsonResponse

def BusinessPostCreate(request):
    if request.method == 'GET':
        context = {
            
        }
        return render(request, 'user/business_post_create.html', context)
    if request.method == 'POST':
        content = request.POST.get('content', '')
        image1 = request.FILES.get('image1', '')
        image2 = request.FILES.get('image2', '')
        image3 = request.FILES.get('image3', '')
        image4 = request.FILES.get('image4', '')
        video = request.FILES.get('video', '')

        user = UserModel.objects.get(id =request.user.id)

        business = BusinessModel.objects.get(owner_id = user.id)

        post = BusinessPostModel.objects.create(
            author=user,
            business=business,
            content=content,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
            video=video,
            country = user.country,
        )
        post.save()

        messages.success(request, "Post created successfully!")
        return redirect(f'/business/page/profile/{business.id}/')
    
def BusinessPostDetails(request,id):
    post = BusinessPostModel.objects.get(id=id)
    comments = BusinessPostCommentModel.objects.filter(post=post).order_by('-created_at')
    context = {
        'post': post,
        'comments': comments,
        }
    return render(request, 'user/business_post_details.html', context)

def BusinessPostComment(request,id,page):
    post = BusinessPostModel.objects.get(id=id)
    if request.method == 'POST':
        comment = BusinessPostCommentModel.objects.create(
            author =request.user,
            post = post,
            content = request.POST.get('content')
        )
        comment.save() 
        return redirect(f'/business/post/details/{id}/') if page == "details" else redirect('/marketplace/')

def BusinessPostReaction(request, id):
    post = BusinessPostModel.objects.get(id=id)
    if request.user in post.reaction.all():
        post.reaction.remove(request.user)
        message = 'Like removed'
    else:
        post.reaction.add(request.user)
        message = 'Like added'
    return JsonResponse({'message': message})