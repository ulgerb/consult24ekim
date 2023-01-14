from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *


def index(request):
    context={'pageinfo': 'Home' }
    
    return render(request,'index.html', context)

def About(request):
    context = {'pageinfo': 'About'}
    return render(request,'about.html', context)

def Services(request):
    context = {'pageinfo': 'Services'}
    return render(request,'service.html', context)

def Contact(request):

    if request.method == "POST":
        user = request.POST["user"]
        email = request.POST["email"]
        title = request.POST["title"]
        text = request.POST["text"]

        contact = Contacts(user=user,email=email,title=title,text=text)
        contact.save()
        return redirect('index')
    
    context = {'pageinfo': 'Contact'}
    return render(request,'contact.html', context)

def Detail(request,id):
    context = {'pageinfo': 'Detail'}
    post = Post.objects.get(id=id)
    categorys = Category.objects.all()
    tagname = Tagname.objects.all()
    posts_random = Post.objects.all().order_by('?')[:3]
    comments = Comment.objects.filter(post=post)
    
    
    if request.method == "POST":
        user = request.POST["user"]
        email = request.POST["email"]
        title = request.POST["title"]
        comment = request.POST["comment"]
        
        comm = Comment(user=user, email=email, title= title, text=comment, post=post)
        comm.save()
        return HttpResponseRedirect('/Detail/'+id+'/')
    
    context.update({'post': post, "categorys": categorys,
                   "tagname": tagname, "posts_random": posts_random,
                    "comments": comments})
    return render(request,'detail.html', context)


# PAGES
def Blog(request,category="all"):
    context = {'pageinfo': 'Blog'}
    
    if category == "all":
        posts = Post.objects.all().order_by('-id')
    else:
        filt = Category.objects.get(category=category)
        posts = Post.objects.filter(category=filt.id).order_by('-id')
        
        
    categorys = Category.objects.all()
    tagname = Tagname.objects.all()
    posts_random = Post.objects.all().order_by('?')[:3]
    
    context.update(
        {"posts": posts, "categorys": categorys, "tagname": tagname, "posts_random": posts_random})
    return render(request, 'pages/blog.html', context)

def Feature(request):
    context = {'pageinfo': 'Feature'}
    return render(request,'pages/feature.html', context)

def Quote(request):
    context = {'pageinfo': 'Quote'}
    return render(request,'pages/quote.html', context)

def Team(request):
    context = {'pageinfo': 'Team'}
    return render(request,'pages/team.html', context)

def Testimonial(request):
    context = {'pageinfo': 'Testimonial'}
    return render(request,'pages/testimonial.html', context)