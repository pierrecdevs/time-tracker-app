from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def privacy(request):
    return render(request,'core/privacy.html')

def terms(request):
    return render(request,'core/terms.html')

def plans(request):
    return render(request,'core/plans.html')
