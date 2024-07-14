
from django.urls import path
from . import views
from .views import HomeView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', views.AboutView, name='about'),
    #path('contact/', views.ContactView, name='contact'),
]




