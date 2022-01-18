from django import forms
  
from .models import Studentdata

class StudentForm(forms.ModelForm):

    class Meta:
        model = Studentdata
        fields = ('proimg','phone','address','institute')