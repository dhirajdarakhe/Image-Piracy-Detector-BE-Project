from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.views import Home

# Create your views here.
def Dashboard(request):
    if not request.user.is_authenticated: 
        messages.warning(request,"Login First!")
        return redirect(Home)
    else:
        return render(request,"dashboard.htm")