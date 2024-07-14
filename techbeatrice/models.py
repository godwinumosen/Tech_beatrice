from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

#The search button model of locatin
    
# The main model for The techbeatrice Model category
class TechbeatricePostModel(models.Model):
    techbeatrice_title = models.CharField(max_length =255, blank=True, null=True)
    techbeatrice_cost_price = models.IntegerField(default ='0', blank=True, null=True)
    techbeatrice_description = models.TextField()
    techbeatrice_img = models.ImageField(upload_to ='tech_images/',blank=True,null=True)
    techbeatrice_slug = models.SlugField (max_length =255,blank=True, null=True)
    techbeatrice_publish_date = models.DateTimeField (auto_now_add= True)
    techbeatrice_author = models.ForeignKey(User, on_delete=models.CASCADE)

         
    class Meta:
        ordering =['-techbeatrice_publish_date']
    
    def __str__(self):
        return self.techbeatrice_title + ' | ' + str(self.techbeatrice_author)
    
    def get_absolute_url(self):
        return reverse('home')