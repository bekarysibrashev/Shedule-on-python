from django.shortcuts import render
from .models import Schedule2
# Create your views here.


def index(request):
    return render(request, "App/index.html")


def PO_1_21b(request):
    schedule = Schedule2.objects.all()[:6]
    return render(request, "secondcourse/po-1-21.html", {"schedule":schedule})

def BNGS_1_21b(request):
    schedule = Schedule2.objects.all()[6:12]
    return render(request, "secondcourse/bngs-1-21.html", {"schedule":schedule})

def ES_1_21b(request):
    schedule = Schedule2.objects.all()[12:18]
    return render(request, "secondcourse/ec-1-21.html", {"schedule":schedule})
    
def ENGM_1_21b(request):
    schedule = Schedule2.objects.all()[18:24]
    return render(request, "secondcourse/engm-1-21.html", {"schedule":schedule})

def MEX_1_21b(request):
    schedule = Schedule2.objects.all()[24:30]
    return render(request, "secondcourse/mex-1-21.html", {"schedule":schedule})

def MEX_2_21b(request):
    schedule = Schedule2.objects.all()[30:36]
    return render(request, "secondcourse/mex-2-21.html", {"schedule":schedule})

def ES_2_21b(request):
    schedule = Schedule2.objects.all()[36:42]
    return render(request, "secondcourse/ec-2-21.html", {"schedule":schedule})
    
def TDNG_1_21b(request):
    schedule = Schedule2.objects.all()[42:48]
    return render(request, "secondcourse/tdng-1-21.html", {"schedule":schedule})

def XTP_11_21b(request):
    schedule = Schedule2.objects.all()[48:54]
    return render(request, "secondcourse/xtp-11-21.html", {"schedule":schedule})

def XTP_1_21b(request):
    schedule = Schedule2.objects.all()[54:60]
    return render(request, "secondcourse/xtp-1-21.html", {"schedule":schedule})

def AIY_1_21b(request):
    schedule = Schedule2.objects.all()[60:66]
    return render(request, "secondcourse/aiy-1-21.html", {"schedule":schedule})