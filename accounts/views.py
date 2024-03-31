from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from panel.views import Dashboard

# Create your views here.

def register(request, params):
    if params["password"] == params["cpassword"]:
        if User.objects.filter(username=params["email"]).exists():
            messages.warning(request, 'EmailId already taken')
        else:
            user = User.objects.create_user(username=params["email"], password=params["password"], email=params["email"])
            user.save()
            messages.success(request, "Registered successfully! Please login now")
    else:
        messages.warning(request, 'Password do not Match')

def Home(request):
    params = dict()
    if request.method == "POST":
        if request.POST["method"] == "Login":
            params = {
                "email" : request.POST["email"],
                "password" :  request.POST["password"]
            }
            if User.objects.filter(email=params["email"]).exists():
                _user = User.objects.get(email=params["email"])
                user = auth.authenticate(username=_user.username, password=params["password"])
                if user is not None:
                    auth.login(request, user)
                    return redirect(Dashboard)
                else:
                    messages.error(request, "Invalid Credentials")
            else:
                messages.error(request, "User does not exist")
        else:
            params = {
                "email" : request.POST["email"], 
                "password" : request.POST["password"], 
                "cpassword" : request.POST["cpassword"]
            }
            register(params)
    return render(request,"home.htm", context={"title":"Home", "params" : params})