
from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,SecondTechbeatriceDetailViewArticleDetailView,InstructorView
from .views import InstructorArticleDetailView,Techbeatrice_Courses,Under_enroll
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('article2/<int:pk>/', SecondTechbeatriceDetailViewArticleDetailView.as_view(), name="second_detail"),
    path('about/', views.AboutView, name='about'),
    path('instructor/', InstructorView.as_view(), name='instructor'),
    path('instructor_article2/<int:pk>/', InstructorArticleDetailView.as_view(), name="instructor_detail"),
    path('contact/', views.ContactView, name='contact'),
    path('techbeatrice_courses/', Techbeatrice_Courses.as_view(), name='techbeatrice_courses'),
    path('message/', views.message, name='message'),
    #path('enroll_application/', views.Techbeatrice_Enroll, name='enroll_application'),
    path('under_enrol/', Under_enroll.as_view(), name='under_enrol'),
    path('it_support/', views.ItSupport, name='it_support'),
    path('it_repairs/', views.ItRepairs, name='it_repairs'),
    path('it_procurement_and_sales/', views.ItProcurementAndSales, name='it_procurement_and_sales'),
    path('general_it_services/', views.GeneralITServices, name='general_it_services'),
    path('incindent_response/', views.IncidentResponse, name='incindent_response'),
    path('managedsecurityservices/', views.ManagedSecurityServices, name='managedsecurityservices'),
]




