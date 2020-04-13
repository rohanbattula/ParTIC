from django import forms
from .models import Party
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PartyForm(forms.ModelForm):

    class Meta:
        model = Party
        fields = ('name', 'address', 'status', 'distance','dateTime','guysAllowed','photo')

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=10, required=True,
                                help_text='To identify yourself')
    email = forms.EmailField(max_length=150, required=True,
                            help_text='Please use your UCLA email')
    class Meta:
        model = User
        fields = ('username', 
            'email', 'password' )
