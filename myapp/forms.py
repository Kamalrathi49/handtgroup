from django import forms
from django.forms.widgets import EmailInput, TextInput, Textarea
from myapp.models import *

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Name'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
     'class': 'form-control', 'placeholder': 'Email'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
     'class': 'form-control', 'placeholder': 'Message'
    }))

    class Meta:
        model = contact
        fields = ('name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        # Call to ModelForm constructor
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for fieldname in ['name', 'email', 'message']:
            self.fields[fieldname].help_text = None

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = subscription
        fields = ('email',)

    