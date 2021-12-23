from django.shortcuts import render

def home(request):
    return render(request,"Facebook_Login/index.html")

# Create your views here.
