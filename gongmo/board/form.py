from  django import forms
from .models import Board
class BoardWriteForm(forms.ModelForm):
    class Meta:
        model= Board
        fields=['title','content','user']
        widgets={
            'title':forms.TextInput(attrs={'class':'title'}),
            'content':forms.TextInput(attrs={'class':'content'}),
            'user':forms.HiddenInput()
        }
        
        