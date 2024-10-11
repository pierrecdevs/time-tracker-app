import string, secrets

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.team.utilities import send_invitation, send_invitation_accepted

# Create your views here.
from .models import Invitation, Team

@login_required
def team(request, team_id):
    team = get_object_or_404(
        Team,
        pk=team_id,
        status=Team.ACTIVE,
        members__in=[request.user]
    )
    invitations = team.invitations.filter(status=Invitation.INVITED)

    return render(request, 'team.html', {'team': team, 'invitations': invitations})

@login_required
def activate_team(request, team_id):
    team = get_object_or_404(
        Team,
        pk=team_id,
        status=Team.ACTIVE,
        members__in=[request.user]
    )

    userprofile = request.user.userprofile
    userprofile.active_team_id = team.id
    userprofile.save()


    messages.info(request, 'Team activated')
    return redirect('team:team', team_id=team.id)

@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team = Team.objects.create(title=title, created_by=request.user)
            team.members.add(request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()
            return redirect('myaccount')

    return render(request, 'add.html')

@login_required
def edit(request):
    team = get_object_or_404(
        Team,
        pk=request.user.userprofile.active_team_id,
        status=Team.ACTIVE,
        members__in=[request.user]
    )

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team.title = title
            team.save()

            messages.info(request, 'Changes were saved')
            return redirect('team:team', team_id=team.id)

    return render(request, 'edit.html', {'team': team})

@login_required
def invite(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)

    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            invitations = Invitation.objects.filter(team=team, email=email)

            if not invitations:
                letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
                code = ''.join(secrets.choice(letters) for i in range(13))
                invitation = Invitation.objects.create(team=team, email=email, code=code)

                messages.info(request, 'The user was invited')
                send_invitation(email, code, team)

                return redirect('team:team', team_id=team.id)
            else:
                messages.info(request, 'The user has already been invited')

    return render(request, 'invite.html', { 'team':team })

