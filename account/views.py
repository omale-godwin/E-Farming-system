from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User 
from .models import Brofile
from django.contrib.auth.decorators import login_required
from listings.models import Listing

from django.contrib.auth import logout


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
 
        if user is not None:

            auth.login(request, user)
            current_user = request.user
            print(current_user.username)
            messages.success(request, 'You are now logged in')
            return redirect('searches')
            
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
   

def register(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        password = request.POST['pass']
        password2 = request.POST['pass2']

        if password == password2:
             if User.objects.filter(username=username).exists():
                 messages.error(request, 'these email have been taken')
                 return redirect(register)
             else:
                 user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                 user.save()
                 messages.success(request, 'You Have Register Successfuuly')
                 return redirect('login')
        else:
             messages.error(request, 'password did not match retry again')
             return redirect('register')
        

    else:
        return render(request, 'account/register.html')
    return render(request, 'account/register.html')


@login_required(login_url='/')
def dashboard(request):
    return render(request, 'account/dashboard.html')


@login_required(login_url='/')
def dashcontact(request):
    return render(request, 'account/dashcontact.html')

@login_required(login_url='/')
def dashview(request):
    data = Listing.objects.all().filter(user=request.user)
    context = {
      'data': data
    }
    return render(request, 'account/dashview.html', context)

@login_required(login_url='/')
def dashpaid(request):
    return render(request, 'account/dashpaid.html')


@login_required(login_url='/')
def profile(request):
    if request.method == 'POST' and request.FILES['myfile']:

        name = request.POST['fullname']
        Nickname  = request.POST['nickname']
        phone = request.POST['phone']
        state = request.POST['state']
        email = request.POST['email']
        local_goverment = request.POST['local_goverment']
        address = request.POST['address']
        city = request.POST['city']
        dob = request.POST['dob']
        date = request.POST['date']
        photo_main = request.FILES['myfile']

       
        
        profiledata = Brofile(fullname=name, nickname=Nickname, dob=dob, date=date, 
        phone=phone, state=state, email=email,city=city, local_goverment=local_goverment, address=address, photo_main=photo_main,  user = request.user)
       
        # profiledata.user = request.user.username
        profiledata.save()
        messages.success(request, 'successfully')
        return redirect('dashboard')
    else:
        print(request.user.username)
        return render(request, 'account/profile.html')
  
    return render(request, 'account/profile.html')
        
       