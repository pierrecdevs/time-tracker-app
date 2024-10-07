from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')

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

