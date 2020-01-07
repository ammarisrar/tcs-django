from django.shortcuts import render

# Create your views here.

def viewTrackingPage(request):
    return render(request, "track/track.html")