from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from . import forms
from dotenv import load_dotenv
import os
from django.http import JsonResponse
from consultancy.models import Training

load_dotenv()

# Create your views here.

def home(request):
    """
     Returns the home page of the application.
    """
    trainings = Training.objects.all()
    data = {}
    data['trainings'] = trainings
    return render(request,'consultancy/index.html',context=data)

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

            content = f"""Dear Site Owner,
            A new submission has been received from your website's contact form. The details of the submission are as follows:

            Name: {name}
            Email: {email}
            Message: {message}

            Please take the necessary actions to respond to the inquiry as soon as possible.
            """

            send_mail(subject=subject,message=content,from_email=None,recipient_list=[os.getenv('DEFAULT_FROM_EMAIL')],fail_silently=False)
            return JsonResponse({
                'status':'Success',
                'message' : 'Mail has been successfully sent'
            })

    return JsonResponse({
        'status':'Failed',
        'message' : 'Mail sending has been failed'
    })
