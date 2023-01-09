from django.shortcuts import render

# Create your views here.


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
    context = {'pageinfo': 'Contact'}
    return render(request,'contact.html', context)

def Detail(request):
    context = {'pageinfo': 'Detail'}
    return render(request,'detail.html', context)

# PAGES
def Blog(request):
    context = {'pageinfo': 'Blog'}
    return render(request,'pages/blog.html', context)

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