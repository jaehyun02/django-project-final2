from django import forms

from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model= Member
        fields=['username','password']
        widgets={
            'password':forms.PasswordInput
        }

class SignupForm(forms.ModelForm):
    password_check = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={'class':'pw2'}))
    
    class Meta:
        model = Member
        fields=['username','password','password_check','name']
        widgets={
            'username':forms.TextInput(attrs={'class':'username'}),
            'password':forms.PasswordInput(attrs={'class':'pw1'})
        }