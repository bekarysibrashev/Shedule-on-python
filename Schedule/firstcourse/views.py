from django.shortcuts import render
from .models import Schedule1
# Create your views here.


def index(request):
    return render(request, "App/index.html")



def ENGM_1_22(request):
    schedule = Schedule1.objects.all()[:6]
    return render(request, "firstcourse/engm-1-22.html", {"schedule":schedule})

def ENGM_2_22(request):
    schedule = Schedule1.objects.all()[6:12]
    return render(request, "firstcourse/engm-2-22.html", {"schedule":schedule})

def XTP_1_22(request):
    schedule = Schedule1.objects.all()[12:18]
    return render(request, "firstcourse/xtp-1-22.html", {"schedule":schedule})
    
def XTP_2_22(request):
    schedule = Schedule1.objects.all()[18:24]
    return render(request, "firstcourse/xtp-2-22.html", {"schedule":schedule})

def XTP_3_22(request):
    schedule = Schedule1.objects.all()[24:30]
    return render(request, "firstcourse/xtp-3-22.html", {"schedule":schedule})


def ES_1_22(request):
    schedule = Schedule1.objects.all()[30:36]
    return render(request, "firstcourse/ec-1-22.html", {"schedule":schedule})

def ES_2_22(request):
    schedule = Schedule1.objects.all()[36:42]
    return render(request, "firstcourse/ec-2-22.html", {"schedule":schedule})

def AIY_1_22(request):
    schedule = Schedule1.objects.all()[42:48]
    return render(request, "firstcourse/aiy-1-22.html", {"schedule":schedule})
    
def AIY_2_22(request):
    schedule = Schedule1.objects.all()[48:54]
    return render(request, "firstcourse/aiy-2-22.html", {"schedule":schedule})

def MEX_1_22(request):
    schedule = Schedule1.objects.all()[54:60]
    return render(request, "firstcourse/mex-1-22.html", {"schedule":schedule})

def MEX_2_22(request):
    schedule = Schedule1.objects.all()[60:66]
    return render(request, "firstcourse/mex-2-22.html", {"schedule":schedule})

def BNGS_1_22(request):
    schedule = Schedule1.objects.all()[66:72]
    return render(request, "firstcourse/bngs-1-22.html", {"schedule":schedule})

def PO_1_22(request):
    schedule = Schedule1.objects.all()[72:78]
    return render(request, "firstcourse/po-1-22.html", {"schedule":schedule})

def PO_2_22(request):
    schedule = Schedule1.objects.all()[78:84]
    return render(request, "firstcourse/po-2-22.html", {"schedule":schedule})

def PO_3_22(request):
    schedule = Schedule1.objects.all()[84:90]
    return render(request, "firstcourse/po-3-22.html", {"schedule":schedule})

def TDNG_1_22(request):
    schedule = Schedule1.objects.all()[90:96]
    return render(request, "firstcourse/tdng-1-22.html", {"schedule":schedule})
