from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Contact
# Create your views here.
from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email  = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contactdata = Contact(fullname=name, email=email, phone=phone, subject=subject, description=messages)
        contactdata.save()
        if contactdata.save():
            messages.success(request, 'you cantact info submitted')
            return redirect('index')
        else:
            messages.error(request, 'unsuccessfully')
            return redirect('contact')
               
    return render(request, 'contact/contact.html')
