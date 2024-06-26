from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .admin import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        print("here")
        if form.is_valid():
                print("valid")
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                password = form.cleaned_data['password']
                username = email.split("@")[0]
                print(first_name,last_name,email)
                
                user = Account.objects.create_user(first_name = first_name,last_name = last_name,email = email,password = password,username = username)
                user.phone_number = phone_number
                user.save()
                messages.success(request,"Registration successful")
                return redirect("register")
    else:
        form = RegistrationForm()
    context = {
    'form' : form,
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        

        user = auth.authenticate(email = email,password = password)
        print(user,"user")
        
        if user is not None:
            auth.login(request,user)
            # messages.success(request,"you are logged in")
            print("success")
            return redirect('home')
        else:
            messages.error(request,'invalid  login credentials')
            print("failure")
            return redirect('login')
    return render(request,'accounts/login.html')
    
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are logged out')
    
    return redirect('login')
    