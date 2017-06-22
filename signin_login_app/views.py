from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User
from .forms import SignUp


def login(request):
    return HttpResponse('This is login page')


def signup(request):
    page = loader.get_template('signin_login_app/signup.html')
    form  = SignUp()
    context = {'form': form}
    return HttpResponse(page.render(context, request))


def signup_(request):
    form = SignUp(request.POST)
    if form.is_valid():
        user_data = form.cleaned_data
        user = User()
        user.name = user_data['name']
        user.user_name = user_data['username']
        user.password = user_data['password']
        user.email = user_data['email']
        user.qualification = user_data['qualification']
        user.date_of_birth = user_data['date_of_birth']
        user.save()
        return HttpResponse('Added ....')
    else:
        context = {'form': form}
        return render(request, 'signin_login_app/signup.html', context)

