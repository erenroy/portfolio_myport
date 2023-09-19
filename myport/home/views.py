from django.shortcuts import render , HttpResponse , redirect
from home.models import Contact
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render
from django.conf import settings
import os
#from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

from .models import Myprojects
# Create your views here.
def home(request):
    return render(request, 'home/index.html')
    
def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
#        print("We are using post request")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
#        print(name,email,phone)
#        content = request.POST['content']
#        print(name,phone,content,email)

        if len(name)<2 or len(email)<3 or len(phone)<10 :
            messages.error(request, "Please fill the form correctly ! ")
        else:
            contact = Contact(name=name, email=email , phone=phone )
            contact.save()
            messages.success(request, "your message has been sent ")
        
    return render(request, 'home/contact.html')

def search(request):
    return render(request, 'home/search.html')

def projects(request):
    allPosts = Myprojects.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/projects.html',context)



def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,
        password=loginpassword)

        if user is not None:
            login(request , user)
            messages.success(request, "Successfully logggedd in ")
            return redirect('home')
        
        else:
            messages.error(request, "invalid syntax , please try aggain ")
            return redirect('home')


# signup handeling starts here 
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        # check for  erroneous  inputs
        if len(username) >  10:
            messages.success(request,"Your usser  name musstt be less thann 10")
            return redirect('home') 

        if not username.isalnum():
            messages.warning(request,"Your usser  name should't contain $ like this")
            return redirect('home')

        if pass1 != pass2:    
            messages.success(request,"Enter correct password")
            return redirect('home')

        #creat the userss
        myuser = User.objects.create_user(username,email , pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request,"Your icoder accouunt has succesfull created")
        return redirect('/')
    else:
        return HttpResponse("404 Error - not found")
    
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logggedd Out ")
    return redirect('home')


# from django.http import FileResponse
# from django.shortcuts import render
# from django.conf import settings
# import os

# def download_pdf(request):
#     pdf_filename = 'Marvel.pdf'  # Replace with your PDF file name
#     pdf_path = os.path.join(settings.STATIC_ROOT, 'pdf', pdf_filename)
#     with open(pdf_path, 'rb') as pdf_file:
#         response = FileResponse(pdf_file, content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
#     return response
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         content = request.POST['content']
# #        print(name,phone,content,email)

#         if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
#             messages.error(request, "Please fill the form correctly ! ")
#         else:
#             contact = Contact(name=name, email=email , phone=phone , content=content)
#             contact.save()
#             messages.success(request, "your message has been sent ")
        
#     return render(request, 'home/contact.html')

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         content = request.POST['content']
# #        print(name,phone,content,email)

#         if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
#             messages.error(request, "Please fill the form correctly ! ")
#         else:
#             contact = Contact(name=name, email=email , phone=phone , content=content)
#             contact.save()
#             messages.success(request, "your message has been sent ")
        
#     return render(request, 'home/contact.html')

