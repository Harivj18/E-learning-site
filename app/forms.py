from .models import page
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
#from django.contrib.auth import models
from .models import comment
#from django.forms.fields import Fields

class Registrationform(UserCreationForm):
    password2 :forms.PasswordInput(attrs={'placeholder':'Enter Your Password'})
    class Meta:
        model=User
        fields=['username',
                 'email'  ,'password1','password2' ]
        widgets={
            'username' : forms.TextInput(attrs={'class':'input'}),
           # 'email' : forms.EmailInput(attrs={'placeholder':'Enter Mail Id'}),
            'password1' : forms.PasswordInput(attrs={'placeholder':'Enter Your Password'}),
            #'password2' : forms.PasswordInput(attrs={'placeholder':'Confirm Your Password'}),

        }

        
        def save(self,commit=True):
           user=super(Registrationform.self).save(commit=False) 
           user.username=self.cleaned_data['username']
           user.email=self.cleaned_data['email']
           if commit:
            user.save()
           return user      


class Myform(forms.ModelForm):
    class Meta:
        model=page
        fields="__all__"

    


class Editprofileform(UserChangeForm):
    class Meta:
        model=User
        fields=['email']

class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields="__all__"