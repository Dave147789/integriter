from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


#Les imports copier pour l'authentification
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseForbidden
from django.template.loader import render_to_string
from django.core.mail import send_mail

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import codecs

from django.contrib.auth.password_validation import validate_password



# Create your views here.

def signup(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()

        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('login')

            #print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
    return render(request, 'accounts/signup.html', context)

def login_user(request):
    error = False
    message = ""
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('index')
            else:
                error = True
                message = "Information Incorrect"

        else:
            error = True
            message = "Information Incorrect"
    
    context = {
        'error':error,
        'message':message
    }

    return render(request, 'accounts/login.html', context)

    
def logout_user(request):
    logout(request)
    return redirect('login')



