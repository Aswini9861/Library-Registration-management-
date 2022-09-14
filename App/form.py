from cProfile import label
from django import forms
from .models import Book, registration

class RegForm(forms.ModelForm):
    class Meta:
        password=forms.CharField(widget=forms.PasswordInput)
        model=registration
        widgets={'pwd':forms.PasswordInput()}
        fields=['email','pwd']


class LoginForm(forms.Form):
    email=forms.EmailField(max_length=30)
    pwd=forms.CharField(widget=forms.PasswordInput())



class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=("ISBN","title","auther","edition")

        labels= {
                 'title':'Title',
                 'auther'  :'Auther',
                 "edition":"Edition"
        }
    def __init__(self,*args,**kwargs):
         super(BookForm,self).__init__(*args,**kwargs)
         self.fields['edition'].required=False