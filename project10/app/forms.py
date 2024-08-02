from django import forms
from .models import *
def validation_for_a(data):
    if data.startswith('a'):
        raise forms.ValidationError('should not start with a')
    

def validation_for_len(data):
    if len(data) <= 5:
        raise forms.ValidationError('Length is lessthan 5')


class SchoolForm(forms.Form):
    sname = forms.CharField(max_length=50, required=False, validators=[validation_for_a, validation_for_len])
    princy = forms.CharField(max_length=25, required=False)
    contact=forms.CharField(max_length=20, required=False)
    loc = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'cols': 30, 'rows': 10}))

class StudentForm(forms.Form):
    sname = forms.ModelChoiceField(queryset=School.objects.all())
    stdname = forms.CharField( max_length=25, required=False)
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'pno']
        # exclude=['pno']


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 5 and name[0] !='a':
            return name
        return None
    
    def clean_pno(self):
        pno = self.cleaned_data['pno']
        if 10<= len(pno) <= 14:
            return pno
        return None