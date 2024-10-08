from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from apps.team.models import Team


@login_required
def myaccount(request):
    user_profile = getattr(request.user, 'userprofile', None)
    if user_profile and user_profile.active_team_id:
        teams = request.user.teams.exclude(pk=request.user.userprofile.active_team_id)
        return render(request, 'myaccount.html', {'teams': teams})
    else:
        return render(request, 'myaccount.html', {'teams': None})

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

