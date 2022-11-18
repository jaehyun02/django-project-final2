from django import forms

from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model= Member
        fields=['nickname','password']
        widgets={
            'password':forms.PasswordInput
        }

class SignupForm(forms.ModelForm):
    password_check = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={'class':'pw2'}))
    
    class Meta:
        model = Member
        fields=['nickname','password','password_check','name']
        widgets={
            'nickname':forms.TextInput(attrs={'class':'nickname'}),
            'password':forms.PasswordInput(attrs={'class':'pw1'})
        }