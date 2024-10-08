from .models import Team

def active_team(request):
    user_profile = getattr(request.user, 'userprofile', None)
    if request.user.is_authenticated:
        if user_profile and user_profile.active_team_id:
            team = Team.objects.get(pk=request.user.userprofile.active_team_id)

            return {'active_team': team}

    return {'active_team': None}
