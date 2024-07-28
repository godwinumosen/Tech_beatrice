from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import Techbeatrice_Courses_PostModel,Techbeatrice_Subjects,Techbeatrice_Instructor,Courses
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
'''def home (request):
    return render (request, 'techbeatrice/home.html' )'''
def base (request):
    return render(request,"base.html")

# The Contact view been implemented
def ContactView (request):
    email='info@techbea.com'
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message'] 
        messages.success(request, f'Your email was Successfully sent to Deus Magnus {message_name}..!')
        return redirect('/message')
    else:
        context={
            'email':email
        } 
        return render(request, 'techbeatrice/contact.html', {})
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
    
 #The first Techbeatrice ArticleDetailView page.
class ArticleDetailView(DetailView):
    model = Techbeatrice_Subjects
    template_name = 'techbeatrice/article_detail.html'
    def ArticleDetailView(request, pk):  
        object = get_object_or_404(Techbeatrice_Subjects, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})
        
#The second ArticleDetailView page of Techbeatrice group   
class SecondTechbeatriceDetailViewArticleDetailView(DetailView):
    model = Techbeatrice_Courses_PostModel
    template_name = 'techbeatrice/second_article_detail.html'    
    context_object_name = 'second_techbeatrices'
    def SecondTechbeatriceDetailViewArticleDetailView(request, pk):
        object = get_object_or_404(Techbeatrice_Courses_PostModel, pk=pk)
        return render(request, 'second_article_detail.html', {'second_detail': object})
    
#About page of the deus magnus blog app
def AboutView (request):
    return render(request, 'techbeatrice/about_us.html', {})
    
#This category is for the Whatsapp API for Techbeatrice
def techbeatrice_whatsapp_message(request):
    techbeatrice_whatsapp_number = '+23480'
    techbeatrice_whatsapp_link = f'https://api.whatsapp.com/send?phone={techbeatrice_whatsapp_number}'
    context = {'whatsapp_link': techbeatrice_whatsapp_link}
    return render(request, 'techbeatrice_kwhatsapp_message.html', context)

def message (request):
    return render (request, 'techbeatrice/message.html', {})

#the InstructorView for techbeatrice page
class InstructorView(ListView): 
    model = Techbeatrice_Instructor 
    template_name = 'techbeatrice/instructor.html' 

#The Techbeatrice Instructor ArticleDetailView page.
class InstructorArticleDetailView(DetailView):
    model = Techbeatrice_Instructor
    template_name = 'techbeatrice/instructor_article_detail.html'
    def InstructorArticleDetailView(request, pk):  
        object = get_object_or_404(Techbeatrice_Instructor, pk=pk)
        return render(request, 'instructor_article_detail.html', {'detail': object})
    
#the Techbeatrice_Courses for techbeatrice navbar link
class Techbeatrice_Courses(ListView): 
    model = Courses 
    template_name = 'techbeatrice/courses.html' 
