# Register your models here.
from django.contrib import admin
# Register your models here.
from . import models
from .models import Techbeatrice_Subjects,Techbeatrice_Courses_PostModel

#The Techbeatrice_Subjects post model admin of Techbeatrice
class Techbeatrice_SubjectsModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'techbeatrice_subjects_slug': ('techbeatrice_subjects_title',)}
    list_display = ['techbeatrice_subjects_title','techbeatrice_subjects_description',
                    'techbeatrice_subjects_img','techbeatrice_subjects_author']
admin.site.register(Techbeatrice_Subjects, Techbeatrice_SubjectsModelAdmin)

#The Techbeatrice_Courses post model admin of Techbeatrice
class Techbeatrice_Courses_ModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'techbeatrice_courses_slug': ('techbeatrice_courses_title',)}
    list_display = ['techbeatrice_courses_title','techbeatrice_courses_description',
                    'techbeatrice_courses_img','techbeatrice_courses_author','techbeatrice_courses_cost_price']
admin.site.register(Techbeatrice_Courses_PostModel, Techbeatrice_Courses_ModelAdmin)