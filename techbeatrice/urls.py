
from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,SecondTechbeatriceDetailViewArticleDetailView,InstructorView
from .views import InstructorArticleDetailView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('article2/<int:pk>/', SecondTechbeatriceDetailViewArticleDetailView.as_view(), name="second_detail"),
    path('about/', views.AboutView, name='about'),
    path('instructor/', InstructorView.as_view(), name='instructor'),
    path('instructor_article2/<int:pk>/', InstructorArticleDetailView.as_view(), name="detail"),
    path('contact/', views.ContactView, name='contact'),
    path('message/', views.message, name='message'),
]




