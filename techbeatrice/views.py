from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'techbeatrice/home.html' )

def base (request):
    return render(request,"base.html")
