# This is home urls

from django.contrib import admin
from django.urls import path , include
from home import views 


from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home , name='home'),
    path('contact', views.contact , name='contact'),
    path('about', views.about , name='about'),
    path('search', views.search , name='search'),
    path('projects', views.projects , name='projects'),
    path('signup', views.handleSignup , name='handleSignup'),
    path('login', views.handleLogin , name='handleLogin'),
    path('logout', views.handleLogout , name='handleLogout'),
#     path('download-pdf/', views.download_pdf, name='download_pdf'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
