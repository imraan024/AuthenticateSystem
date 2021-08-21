from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from users.forms import SignUpForm, UserLoginForm 
from django.contrib.auth.decorators import login_required


#Create your views here.
@login_required(login_url='login/')

def home(request):
    return render(request, "registration/user_information.html")



def register(request):
    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context['register_form']=form

    else:
        form=SignUpForm()
        context['register_form']=form
    return render(request, 'registration/register.html', context)


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'login_form': form,
    }
    return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('login/')


    