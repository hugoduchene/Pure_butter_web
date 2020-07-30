from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import RegistrationForm, LoginForm
from user.models import UserSubscribeEmail
from django.template import loader
from django.http import HttpResponse
from django.core.mail import send_mail
import Pure_butter_web.settings as settings

# Create your views here.
def accountView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            is_exist = UserSubscribeEmail.objects.filter(id_user= request.user)
            if len(is_exist) == 0:
                u = UserSubscribeEmail(id_user= request.user)
                u.save()
                send_mail(
                    'Inscription newsletter',
                    'Bienvenue vous faites parti de nos plus fidèles collaborateurs',
                    settings.env('EMAIL'),
                    [request.user.email],
                    fail_silently=False,
                )
        template = loader.get_template('user/account.html')
        return HttpResponse(template.render(request=request))
    else:
        return redirect('registration')


def registrationView(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('index')
    context = {'form' : form}

    template = loader.get_template('user/registration.html')
    return HttpResponse(template.render(request=request, context=context))
