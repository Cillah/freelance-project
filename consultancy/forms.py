from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(label='name', max_length=100)
  email = forms.EmailField()
  subject = forms.CharField(max_length=100)
  message = forms.CharField(max_length=300)
