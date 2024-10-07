from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from .models import UserProfile

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        print(f"User: {request.user}")
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        messages.info(request, 'Successfully updated account')

        return redirect('myaccount')

    return render(request,'edit_profile.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username
            user.email = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()

            userprofile = UserProfile.objects.create(user=user)
            login(request, user)

            return redirect('frontpage')
        else:
            print(form.errors) # this was debugging. apparently django requires you to use password1 and password2
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
