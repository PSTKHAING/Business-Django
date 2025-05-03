from user.models import *

def BusinessOwnerID(request):
    try:
        my_business_page = BusinessModel.objects.get(owner_id = request.user.id)
    except:
        my_business_page = None
    return {
        "my_business_page":my_business_page
    }

def CurrentBusinessID(request):
    current_business_page = None
    try:
        business_id = request.resolver_match.kwargs.get('id')
        if business_id:
            current_business_page = BusinessModel.objects.get(id=business_id)
    except:
        pass

    return {
        'current_business_page': current_business_page
    }

def PostOwnerID(request):
    try:
        my_post = PostModel.objects.get(owner_id = request.user.id)
    except:
        my_post = None
    return {
        "my_post":my_post
    }

def CurrentPostID(request):
    current_post = None
    try:
        post_id = request.resolver_match.kwargs.get('id')
        if post_id:
            current_post = PostModel.objects.get(id=post_id)
    except:
        pass

    return {
        'current_post': current_post
    }

def CurrentUserID(request):
    current_user = None
    try:
        user_id = request.resolver_match.kwargs.get('id')
        if user_id:
            current_user = UserModel.objects.get(id = user_id)
    except:
        pass

    return{
        "current_user":current_user
    }