# admin.py

from django.contrib import admin
from .models import StudyProgram, Course, Student, Exam, Paper , Question, PaperSubmission, Notification

admin.site.register(StudyProgram)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Paper)
admin.site.register(Question)
admin.site.register(PaperSubmission)
admin.site.register(Notification)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email', 'age', 'study_program', 'date_enrolled')
    search_fields = ('student_id', 'name', 'email', 'study_program') 
    list_filter = ('study_program', 'age')  
