from django import forms
from django.forms import fields
from .models import Teacher
from django.db.models.base import Model

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model= Teacher
        fields= "__all__"