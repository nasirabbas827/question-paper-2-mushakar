from django import forms
from .models import Student

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'password', 'age', 'address', 'date_enrolled', 'study_program']

        
from django import forms
from .models import PaperSubmission

class PaperSubmissionForm(forms.ModelForm):
    class Meta:
        model = PaperSubmission
        fields = ['uploaded_file']
