from django.shortcuts import render

# Create your views here.

def viewpage(request):
    return render(request, 'about/About.html')