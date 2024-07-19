from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import *


def home(request):
    sub = subsection.objects.all()
    main = Mainsection.objects.all()
    if request.method == "POST":
        Name = request.POST['Name']
        cx_email = request.POST['email']
        subject = request.POST['subject']
        feedback = request.POST['feedback']

        send_mail(
            'Name: ' + Name + ', Subject: ' + subject + ', ' + cx_email, # subject
            feedback, # message
            cx_email, # sender's email email
            ['agshards@gmail.com'] # receiver's email
        )
        messages.success(request, ('Thank you for your response!'))
        return render(request, 'home.html', {'main':main, 'sub':sub, 'Name':Name})
    else:
        return render(request, 'home.html', {'main':main, 'sub':sub})

def portfolio(request):
    samples = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'samples': samples})

def detailed(request, id):
    sample = get_object_or_404(Portfolio, id=id)
    img = portfolioImage.objects.filter(portfolio=sample)
    return render(request, 'detailed.html',{'sample':sample, 'img': img})
