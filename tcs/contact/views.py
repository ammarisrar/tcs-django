from django.shortcuts import render

# Create your views here.
def viewContactPage(request):
    return render(request,'contact/contact.html')