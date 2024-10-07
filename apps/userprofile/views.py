from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm

from .models import UserProfile


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
