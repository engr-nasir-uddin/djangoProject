from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("hello bangladesh")
    text= {'title': 'Mr.', 'name': 'Md. Nasir Uddin', 'course': 'Django'}
    return render(request, 'index.html', text)
    
def add(request):
    value1=int(request.POST['num1'])
    value2=int(request.POST['num2'])

    result= value1+value2

    return render(request, 'result.html', {'result': result})

def shop(request):
    return HttpResponse("Welcome to Projukti Shop")
