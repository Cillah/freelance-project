from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from . import forms
from dotenv import load_dotenv
import os
from django.http import JsonResponse

load_dotenv()

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
            send_mail(subject=subject,message=message,from_email=None,recipient_list=[os.getenv('DEFAULT_FROM_EMAIL')],fail_silently=False)
            return JsonResponse({
                'status':'Success',
                'message' : 'Mail has been successfully sent'
            })

    return JsonResponse({
        'status':'Failed',
        'message' : 'Mail sending has been failed'
    })
