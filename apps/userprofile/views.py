from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.team.utilities import send_invitation_accepted

from .models import UserProfile
from apps.team.models import Invitation, Team


@login_required
def myaccount(request):
    # user_profile = getattr(request.user, 'userprofile', None)
    # teams = request.user.teams.exclude(pk=request.user.userprofile.active_team_id)
    # invitations = Invitation.objects.filter(email=request.user.email, status=Invitation.INVITED)
    # if user_profile and user_profile.active_team_id:
    #     teams = request.user.teams.exclude(pk=request.user.userprofile.active_team_id)
    #     return render(request, 'myaccount.html', {'teams': teams, 'invitations': invitations})
    # else:
    #     return render(request, 'myaccount.html', {'teams': None})
    teams = request.user.teams.exclude(pk=request.user.userprofile.active_team_id)
    invitations = Invitation.objects.filter(email=request.user.email, status=Invitation.INVITED)

    return render(request, 'myaccount.html', {'teams': teams, 'invitations': invitations})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        print(f"User: {request.user}")
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        if request.FILES:
            avatar = request.FILES['avatar']
            userprofile = request.user.userprofile
            userprofile.avatar = avatar
            userprofile.save()

        messages.info(request, 'Successfully updated account')

        return redirect('myaccount')

    return render(request,'edit_profile.html')


@login_required
def accept_invitation(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        invitations = Invitation.objects.filter(code=code, email=request.user.email)

        if invitations:
            invitation = invitations[0]
            invitation.status = Invitation.ACCEPTED
            invitation.save()

            team = invitation.team
            team.members.add(request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()

            messages.info(request, 'Invitation accepted.')

            send_invitation_accepted(team, invitation)

            return redirect('team:team', team_id=team.id)
        else:
            messages.info(request, 'Invitation was not found')
    else:
        return render(request, 'accept_invitation.html')
