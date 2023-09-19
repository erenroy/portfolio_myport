# This is blog urls

from django.contrib import admin
from django.urls import path , include
from . import views 

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.blogHome , name="blogHome"),
    # path('<str:slug>', views.blogPost , name="blogPost"),
    path('<slug:post_slug>', views.blogdetails , name='blogdetails'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
