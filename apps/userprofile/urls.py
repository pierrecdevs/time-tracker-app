from django.urls import path

from apps.userprofile.views import edit_profile, myaccount

urlpatterns= [
    path('', myaccount, name='myaccount'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
