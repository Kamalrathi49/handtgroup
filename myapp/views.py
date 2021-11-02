from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def Home(request):
    service = our_service.objects.filter(is_active = True)
    planning = planning_stag.objects.filter(is_active = True)
    project = our_project.objects.filter(is_active = True)
    review = public_review.objects.filter(is_active = True)
    our_property = propertys.objects.filter(is_active = True)
    partner = our_partner.objects.filter(is_active = True)
    address = our_address.objects.filter(is_active = True)
    top_images = top_image.objects.filter(is_active = True)
    ctx= {'services':service, 'plannings':planning, 'projects':project,
        'reviews':review, 'propertys':our_property, 'partners':partner, 'address':address, 'top_image': top_images,}
    return render(request, 'index.html', ctx)

def AboutUs(request):
    planning = planning_stag.objects.all()
    review = public_review.objects.all()
    partner = our_partner.objects.all()
    address = our_address.objects.all()
    ctx = {'plannings':planning, 'reviews':review,'partners':partner, 'address':address,}
    return render(request, 'about-us.html', ctx)

def Services(request):
    service = our_service.objects.all()
    review = public_review.objects.all()
    partner = our_partner.objects.all()
    address = our_address.objects.all()
    ctx = {'services':service, 'reviews':review, 'partners':partner, 'address':address,}
    return render(request, 'services-1.html', ctx)

def OurTeam(request):
    partner = our_partner.objects.all()
    address = our_address.objects.all()
    ctx = {'partners':partner, 'address':address,}
    return render(request, 'team.html', ctx)

def Contact(request):
    if request.method == 'POST':
        contactform  = ContactUsForm(request.POST)
        subscriptionform  = SubscriptionForm(request.POST)
        if contactform.is_valid():
            user = contactform.save()
            user.save()
            subject = 'HANDT GROUP'
            message = f'Hi {user.name}, thanks for contacting HANDT GROUP, How can we help you?'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            print('<<<<<<--------------form saved successfully-------------------->>>>>>')
            return redirect('myapp:contact')
        else:
            print('>>>>>>---------------message not sent-----------------<<<<<<')
            return redirect('myapp:contact')
    else:
        address = our_address.objects.all()
        contactform  = ContactUsForm()
        ctx = {'addresses':address, 'contactform':contactform,'address':address}
        return render(request, 'contact.html', ctx)

def subscribe(request):
    if request.method == 'POST':
        subscriptionform  = SubscriptionForm(request.POST)
        if subscriptionform.is_valid():
            subscriber = subscriptionform.save()
            subscriber.save()
            subject = 'Welcome to HANDT GROUP'
            message = f'Hi, thanks for joing HANDT GROUP'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [subscriber.email, ]
            send_mail( subject, message, email_from, recipient_list )
            print('<<<<<<--------------subscribed successfully-------------------->>>>>>')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            print('>>>>>>---------------subscription failed-----------------<<<<<<')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        redirect(request.META.get('HTTP_REFERER'))

    
def Projects(request):
    project = our_project.objects.all()
    partner = our_partner.objects.all()
    address = our_address.objects.all()
    ctx = {'projects':project, 'partners':partner, 'address':address,}
    return render(request, 'projects.html', ctx)

def ProjectSingle(request, our_project_id):
    project = our_project.objects.filter(id = our_project_id)
    partner = our_partner.objects.all()
    address = our_address.objects.all()
    ctx = {'projects':project, 'partners':partner, 'address':address,}
    return render(request, 'project-single.html', ctx)
    

def Testimonal(request):
    review = public_review.objects.all()
    partner = our_partner.objects.all()
    address = our_address.objects.all()
    ctx = {'partners':partner, 'reviews':review, 'address':address,}
    return render(request, 'testimonial.html', ctx)
