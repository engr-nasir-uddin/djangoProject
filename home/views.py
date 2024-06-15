from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.
def dashboard(request):
    # return HttpResponse("hello bangladesh")
    return render(request, 'home.html')

def home(request):
    # return HttpResponse("hello bangladesh")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("hello bangladesh")
    return render(request, 'about.html')

def blog(request):
    # return HttpResponse("hello bangladesh")
    return render(request, 'blog.html')
    
def contact(request):
    # return HttpResponse("hello bangladesh")
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']

        values=Contact(name=name, email=email, message=message)
        values.save()
        
    return render(request, 'contact.html')
    
    

    return HttpResponse("Welcome to Projukti Shop")
