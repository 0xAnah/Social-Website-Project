from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from .models import Profile


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

@login_required
def dashboard(request):
    context = {'section': 'dashboard'}
    return render(request, 'account/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a user but don't save it yet
            new_user = user_form.save(commit=False)
            # set the user chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            # create the user profile
            Profile.objects.create(user=new_user)

            context = {'new_user': new_user}
            return render(request, 'account/register_done.html', context=context)
    else:
        user_form = UserRegistrationForm()

    context = {'user_form': user_form}
    return render(request, 'account/register.html', context=context)

@login_required
def edit(request):
    if request.method == 'POST':
        # the user has specified what is to be updated
        # so we get the user and update his details
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files= request.FILES)
        pass
    else:
        # the user is just clicking the link to update his profile
        # send the user profile so he can edit
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        #we validate both forms and save them
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error updating your profile')

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'account/edit.html', context=context)
