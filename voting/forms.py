from django import forms
from .models import Student, Candidate, Vote


class CheckRollForm(forms.ModelForm):
    s_grade = forms.IntegerField(label='학년')
    s_class = forms.CharField(label='반')
    s_birth = forms.CharField(label='생년월일')
    s_name = forms.CharField(label='이름')

    class Meta:
        model = Student
        fields = ['s_grade', 's_class', 's_birth', 's_name']