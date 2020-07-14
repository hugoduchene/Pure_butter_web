from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import RegistrationForm, LoginForm
from django.template import loader
from django.http import HttpResponse




# Create your views here.
def accountView(request):
    template = loader.get_template('user/account.html')
    return HttpResponse(template.render(request=request))

def registrationView(request):
    form = RegistrationForm()
    context = {
        'form' : form
    }

    if request.method == 'POST':
        form_req = RegistrationForm(request.POST)
        if form_req.is_valid():
            form_req.save()
            username = form_req.cleaned_data['username']
            password1 = form_req.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('index')
        else:
            pass
    else:
        pass


    template = loader.get_template('user/registration.html')
    return HttpResponse(template.render(request=request, context=context))
