from django.urls import path
from .views import activate_team, add, invite, team, edit

app_name = 'team'

urlpatterns = [
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
    path('invite/', invite, name='invite'),
    path('activate_team/<int:team_id>/', activate_team, name='activate_team'),
    path('<int:team_id>/', team, name='team'),
]
