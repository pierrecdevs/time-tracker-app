from django.urls import path
from .views import activate_team, add, invite, plans, plans_thankyou, team, edit
from .api import stripe_webhook, create_checkout_session

app_name = 'team'

urlpatterns = [
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
    path('invite/', invite, name='invite'),
    path('activate_team/<int:team_id>/', activate_team, name='activate_team'),
    path('<int:team_id>/', team, name='team'),
    path('plans/', plans, name='plans'),
    path('plans/thank_you/', plans_thankyou, name='plans_thankyou'),

    path('api/stripe_webhook/', stripe_webhook, name='stripe_webhook'),
    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
]
