from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms

# Create your views here.

def home(request):
    """
     Returns the home page of the application.
    """
    return render(request,'consultancy/index.html')

def contact(request):
    """
     Function to send email to the site owner, when a user submits the form.
    """
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        #validating the form.
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message'] 

    return redirect("home")