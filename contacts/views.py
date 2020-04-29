from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
import zerosms
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
            listing = request.POST['listing']
            listing_id = request.POST['listing_id']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            time = request.POST['time']
            vehicle = request.POST['vehicle']
            message = request.POST['message']
            user_id = request.POST['user_id']
            listing_email = request.POST['listing_email']


            if request.user.is_authenticated: # check for already made inquiry
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

                if has_contacted:
                    messages.error(request,'You have already booked this Driving Center')
                    return redirect('/listings/'+listing_id)

            else:
                messages.error(request, 'You must be logged in')
                return redirect('login')



            contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, vehicle=vehicle, time=time, phone=phone, message=message, user_id=user_id, listing_email=listing_email,)

            contact.save()

            # SEND MAIL To LISTINGS
            send_mail(
                'Driving Center Booking',
                'Hello, There has been booking in ' + listing + ' for ' + time + '. Sign into the admin panel for more info about booking' + '. Have a good day.',
                'sumancr.marahatha@gmail.com',
                 [listing_email, 'suseelcr7@gmail.com'],
                 fail_silently = False
                )

            # SEND SMS
            # {% csrf_token %}
            # zerosms.sms(phno=+9779843774961, receivernum = [+9779843493701], message='Thank you for booking ' + listing ),
            # return HttpResponse("SEND")

            messages.success(request, 'Your booking request has been submitted, We will get back to you soon')
            messages.success(request, 'Thank you for trusting us')
            return redirect('/listings/'+listing_id)



