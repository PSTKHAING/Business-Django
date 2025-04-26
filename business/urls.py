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

    path('',page_view.Index),
    path('login/',auth_view.LogIn),
    path('logout/',auth_view.LogOut),
    path('profile/post/',page_view.ProfilePost),
    path('profile/about/', page_view.ProfileAbout),
    path('profile/chat/' ,page_view.ProfileChat),
    path('profile/connection/' ,page_view.ProfileConnection),
    path('profile/update/', page_view.ProfileUpdate),
    path('profile/event/' ,page_view.ProfileEvent),
    path('profile/group/', page_view.ProfileGroup),
    path('profile/notification/', page_view.ProfileNotification),
    path('profile/photo/' ,page_view.ProfilePhoto),
    path('profile/video/' ,page_view.ProfileVideo),
    
    path('post/create/',post_view.PostCreate),

    path('business/page/',business_view.BusinessPage),
    path('business/page/create/',business_view.BusinessPageCreate),
    path('business/page/info/',business_view.BusinessPageInfo),
    path('business/page/profile/<int:id>/',business_view.BusinessPageProfile),
    path('business/page/dashboard/', business_view.BusinessPageDashboard),
    path('business/page/your/page/', business_view.BusinessPageYourPage),
    path('business/page/privacy/', business_view.BusinessPagePrivacy),
    path('business/page/setting/', business_view.BusinessPageSetting),
    path('business/page/profile/update/',business_view.BusinessPageProfileUpdate)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)