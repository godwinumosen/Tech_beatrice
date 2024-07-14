from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Techbeatrice_Courses_PostModel,Techbeatrice_Subjects
# Create your views here.
'''def home (request):
    return render (request, 'techbeatrice/home.html' )'''
def base (request):
    return render(request,"base.html")
#The main Techbeatrice HomeView page
class HomeView(ListView): 
    model = Techbeatrice_Courses_PostModel
    template_name = 'techbeatrice/home.html'

#About page of the deus magnus blog app
def AboutView (request):
    return render(request, 'techbeatrice/about_us.html', {})