from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from .forms import Contactform

# Create your views here.

def home(request):
    context ={

    }
    return render(request, 'index.html', context)

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            send_mail(
                subject= 'New Newsletter Subscriber',
                message= f"A new user has subscribed to your newsletter: {email}",
                from_email=None,
                recipient_list=['venrahq@gmail.com'],
            )

            send_mail(
                subject='Welcome to Venra!🌱',
                message="""
Hi there,

Thanks for subscribing to Venra — where innovation meets learning.

We’re thrilled to have you on board. Expect insights, updates, and exclusive drops as we build the future of learning together.

You’re officially part of the journey 🚀

Team Venra,
Empowering learners. One step at a time.
                """,
                from_email=None,
                recipient_list=[email],
            )
            messages.success(request, "You've been subscribed successfully!")
        else:
            messages.error(request, "Please enter a valid email.")

    return redirect('home')

def contact(request):
    form = Contactform
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']


            send_mail(
                subject=f"Contact Form: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\n{message}",
                from_email=None,
                recipient_list=['venrahq@gmail.com'],
            )


            send_mail(
                subject='We got your message 📨',
                message =f"""
Hello {name},

Thanks for reaching out to Venra — your message has been received and is currently being reviewed.

We’ll get back to you as soon as possible.

If your message was urgent, feel free to follow up directly via [your email or social handle].

Cheers,
Team Venra
Driven by simplicity. Designed for learners.
                """,
                from_email=None,
                recipient_list=[email],
            )

            messages.success(request, "Your message was sent successfully!")
            return redirect('home')
    
    return render(request, 'index.html', {'form':form})