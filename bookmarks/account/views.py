from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autheticated Successfully')
                else:
                    return HttpResponse('Account Disabled')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'account/login.html', context=context)
        