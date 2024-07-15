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
    model = Techbeatrice_Subjects 
    template_name = 'techbeatrice/home.html'   

    #This model is for the second Techbeatrice_Courses_PostModel sub category of the home page
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
    #context['user'] = self.request.user
        context['second_techbeatrices'] = Techbeatrice_Courses_PostModel.objects.all()
        return context
    
 #The first Techbeatrice ArticleDetailView page
class ArticleDetailView(DetailView):
    model = Techbeatrice_Subjects
    template_name = 'techbeatrice/article_detail.html'
    def ArticleDetailView(request, pk):  
        object = get_object_or_404(Techbeatrice_Subjects, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})
        

#About page of the deus magnus blog app
def AboutView (request):
    return render(request, 'techbeatrice/about_us.html', {})