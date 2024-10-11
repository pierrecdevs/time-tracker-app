from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_invitation(to_email, code, team):
    from_email = settings.DEFAULT_EMAIL_FROM
    accept_url = settings.ACCEPT_URL

    subject = 'Invitation to FKS Time Tracker'
    text_content = f'Invitaion to FKS Time Tracker. Your code is: {code}'
    html_content = render_to_string('email_invitation.html', {'code': code, 'team': team, 'accept_url': accept_url})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

def send_invitation_accepted(team, invitation):
    from_email = settings.DEFAULT_EMAIL_FROM
    subject = 'Invitation accepted'
    text_content = 'Your invitation was accepted'
    html_content = render_to_string('email_accepted_invitation.html', {'team': team, 'invitation': invitation})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [team.created_by.email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

