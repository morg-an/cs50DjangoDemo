from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
#for authentication:
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# display info about the currently logged in user.
def index(request):
    #.user and .is_authenticated are pre-built in Django
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
    

def login_view(request):
    if request.method == "POST":
        #get the username/password from inside the post data
        username = request.POST["username"]
        password = request.POST["password"]
        #use django built in tools for authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "message": "Login was unsuccessful. Please try again."
            })

    #for get requests, render html w/ login form
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")