from django.contrib.auth import login
from django.shortcuts import redirect, render

from apps.core.forms import CustomUserCreationForm
from apps.team.models import Invitation
from apps.userprofile.models import UserProfile


# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def privacy(request):
    return render(request,'core/privacy.html')

def terms(request):
    return render(request,'core/terms.html')

def plans(request):
    return render(request,'core/plans.html')

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

            invitations = Invitation.objects.filter(email=user.email, status=Invitation.INVITED)

            if invitations:
                return redirect('accept_invitation')
            else:
                return redirect('dashboard')
        else:
            print(form.errors) # this was debugging. apparently django requires you to use password1 and password2
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/signup.html', {'form': form})
