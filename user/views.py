from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import RegistrationForm, LoginForm
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def accountView(request):
    if request.user.is_authenticated:
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
