"""
URL configuration for business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from views.user import page_view,auth_view,post_view,business_view

urlpatterns = [
     path(settings.ADMIN_LOGIN_URL, admin.site.urls),

    #  ADMIN URLS

    #  USER URLS

    path('search/',page_view.Search),
    path('',page_view.Index),
    path('login/',auth_view.LogIn),
    path('logout/',auth_view.LogOut),
    path('profile/chat/<uuid:id>/' ,page_view.ProfileChat),
    path('profile/update/<uuid:id>/', page_view.ProfileUpdate),
    path('profile/notification/<uuid:id>/', page_view.ProfileNotification),
    path('profile/post/<uuid:id>/',page_view.ProfilePost,name="profile_post"),
    path('profile/about/<uuid:id>/', page_view.ProfileAbout,name="profile_about"),
    path('profile/connection/<uuid:id>/' ,page_view.ProfileConnection,name="profile_connection"),
    path('profile/event/<uuid:id>/' ,page_view.ProfileEvent,name="profile_event"),
    path('profile/group/<uuid:id>/', page_view.ProfileGroup,name="profile_group"),
    path('profile/photo/<uuid:id>/' ,page_view.ProfilePhoto,name="profile_photo"),
    path('profile/video/<uuid:id>/' ,page_view.ProfileVideo,name="profile_video"),
    
    path('post/create/',post_view.PostCreate),
    path('post/details/<int:id>/',post_view.PostDetails),
    path('post/reaction/<int:id>/',post_view.PostReaction),
    path('post/comment/<int:id>/<str:page>/',post_view.PostComment,name='post_comment'),

    path('business/page/',business_view.BusinessPage),
    path('business/page/create/',business_view.BusinessPageCreate),
    path('business/page/info/',business_view.BusinessPageInfo),
    path('business/page/profile/<int:id>/',business_view.BusinessPageProfile),
    path('business/page/dashboard/<int:id>/', business_view.BusinessPageDashboard),
    path('business/page/your/page/<int:id>/', business_view.BusinessPageYourPage),
    path('business/page/privacy/<int:id>/', business_view.BusinessPagePrivacy),
    path('business/page/setting/<int:id>/', business_view.BusinessPageSetting),
    path('business/page/profile/update/<int:id>/',business_view.BusinessPageProfileUpdate)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)