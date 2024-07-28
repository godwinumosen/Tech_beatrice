# Register your models here.
from django.contrib import admin
from . import models 
from .models import Techbeatrice_Subjects,Techbeatrice_Courses_PostModel,Techbeatrice_Instructor,Courses
#from .models import 

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

# The Instructor model for The techbeatrice Model category
class Techbeatrice_Instructor_ModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'techbeatrice_instructor_slug': ('techbeatrice_instructor_name',)}
    list_display = ['techbeatrice_instructor_name','techbeatrice_instructor_description','techbeatrice_instructor_img']
admin.site.register(Techbeatrice_Instructor, Techbeatrice_Instructor_ModelAdmin)

# The Courses admin model for The techbeatrice modeAdmin category
class Courses_Admin (admin.ModelAdmin):
    prepopulated_fields = {'courses_slug': ('courses_title',)}
    list_display = ['courses_title','courses_description','courses_img']
admin.site.register(Courses, Courses_Admin)