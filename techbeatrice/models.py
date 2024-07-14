from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Techbeatrice_Subjects(models.Model):      
    techbeatrice_subjects_title = models.CharField(max_length =205, blank=True, null=True)
    techbeatrice_subjects_description = models.TextField()
    techbeatrice_subjects_img = models.ImageField(upload_to ='tech_subjects_img/',blank=True,null=True)
    techbeatrice_subjects_slug = models.SlugField (max_length =205,blank=True, null=True)
    techbeatrice_subjects_publish_date = models.DateTimeField (auto_now_add= True)
    techbeatrice_subjects_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-techbeatrice_subjects_publish_date']
    def __str__(self):
        return self.techbeatrice_subjects_title + ' | ' + str(self.techbeatrice_subjects_author)
    def get_absolute_url(self):
        return reverse('home')

# The main model for The techbeatrice Model category
class Techbeatrice_Courses_PostModel(models.Model):
    techbeatrice_courses_title = models.CharField(max_length =255, blank=True, null=True)
    techbeatrice_courses_cost_price = models.IntegerField(default ='0', blank=True, null=True)
    techbeatrice_courses_description = models.TextField()
    techbeatrice_courses_img = models.ImageField(upload_to ='tech_courses_img/',blank=True,null=True)
    techbeatrice_courses_slug = models.SlugField (max_length =255,blank=True, null=True)
    techbeatrice_courses_publish_date = models.DateTimeField (auto_now_add= True)
    techbeatrice_courses_author = models.ForeignKey(User, on_delete=models.CASCADE)

         
    class Meta:
        ordering =['-techbeatrice_courses_publish_date']
    
    def __str__(self):
        return self.techbeatrice_courses_title + ' | ' + str(self.techbeatrice_courses_author)
    
    def get_absolute_url(self):
        return reverse('home')