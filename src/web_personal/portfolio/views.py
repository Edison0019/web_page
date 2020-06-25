from django.shortcuts import render
from .models import portfolio

# Create your views here.
def portafolio(request):
    prtf = portfolio.objects.all()
    context = {
        'portfolio' : prtf
    }
    return render(request,'portfolio/portafolio.html',context)