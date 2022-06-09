# username = kausarat
# password = kassy2004
from django.http import HttpResponse, response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages 
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pnumber = request.POST['pnumber']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if Profile.objects.filter(email = email) .exists():
                messages.info(request, 'email exist already')
                return redirect('form')
            elif Profile.objects.filter(pnumber = pnumber).exists():
                messages.info(request, 'Phone number exists already')
                return redirect('form')
            else:
                new_profile = Profile.objects.create(fname= fname, lname = lname, email=email, pnumber= pnumber, password=password)
                new_profile.save()
                return redirect('register')
        else:
            messages.info(request, 'password does not match')
            return redirect('form')
    else:
        return render(request, 'form.html')

def register(request):
    return render(request, 'register.html')