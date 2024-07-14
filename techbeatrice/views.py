from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
'''def home (request):
    return render (request, 'techbeatrice/home.html' )'''
def base (request):
    return render(request,"base.html")
#The main Techbeatrice HomeView page
class HomeView(ListView): 
    model = TechbeatricePostModel
    template_name = 'techbeatrice/home.html'
