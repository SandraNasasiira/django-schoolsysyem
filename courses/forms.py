from django import forms
from django.forms import fields
from .models import Courses
from django.db.models.base import Model

class CoursesRegistrationForm(forms.ModelForm):
    class Meta:
        model= Courses
        fields= "__all__"