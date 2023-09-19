# from django.shortcuts import render , HttpResponse

from django.shortcuts import render , redirect , get_object_or_404
from blog.models import Post
from django.views import View

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html' ,context)
    
def blogdetails(request,post_slug):
    post = get_object_or_404(Post , slug=post_slug)
    context = {'post': post}
    return render(request, 'blog/blogdetails.html',context)


# # Create your views here.
# def blogHome(request):
#     allPosts = Post.objects.all()
#     # context = {'allPosts': allPosts}   context
#     return render(request, 'blog/blogHome.html' , )
    
# def blogPost(request, slug):
#     post = Post.objects.filter(slug=slug).first()
# #    print(post)
#     context = {'post': post}
#     return render(request, 'blog/blogPost.html' , context)