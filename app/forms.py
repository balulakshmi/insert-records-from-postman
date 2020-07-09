from django import forms
from app.models import CourseModel
class CourseForm(forms.ModelForm):
    class Meta:
        model=CourseModel
        fields = '__all__'