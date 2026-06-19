from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    oglasi = JobAd.objects.filter(open_until__gte=datetime.now().date())
    return render(request,'index.html', )

@login_required
def details(request):
    oglas = JobAd.objects.filter(id= pk).first()
    aplikanti = Application.objects.filter(job_ad__pk = pk).all()
    aplikant = SystemUser.objects.filter(user=request.user,role='applicant').first()
    )
    return render(request,'details',context=)