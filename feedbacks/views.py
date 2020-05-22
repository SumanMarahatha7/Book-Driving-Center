from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
from django.contrib.auth.models import User

def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        feedback = Feedback(name=name, email= email, message=message)
        feedback.save()

        messages.success(request, 'Thank you for your feedback, Your words means a lot')
        return redirect('/')

    else:
        return render(request, 'pages/feedback.html')
