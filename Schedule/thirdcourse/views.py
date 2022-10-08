from django.shortcuts import render
from .models import Schedule3
# Create your views here.


def index(request):
    return render(request, "App/index.html")


def AIY_1_20(request):
    schedule = Schedule3.objects.all()[:6]
    return render(request, "firstcourse/po-1-21.html", {"schedule":schedule})

def BNGS_1_20(request):
    schedule = Schedule3.objects.all()[6:12]
    return render(request, "firstcourse/bngs-1-21.html", {"schedule":schedule})

def ES_1_20(request):
    schedule = Schedule3.objects.all()[12:18]
    return render(request, "firstcourse/ec-1-21.html", {"schedule":schedule})
    
def ES_2_20(request):
    schedule = Schedule3.objects.all()[18:24]
    return render(request, "firstcourse/engm-1-21.html", {"schedule":schedule})

def ES_3_20(request):
    schedule = Schedule3.objects.all()[24:30]
    return render(request, "firstcourse/mex-1-21.html", {"schedule":schedule})

def ENGM_1_20(request):
    schedule = Schedule3.objects.all()[30:36]
    return render(request, "firstcourse/mex-2-21.html", {"schedule":schedule})

def IS_1_20(request):
    schedule = Schedule3.objects.all()[36:42]
    return render(request, "firstcourse/ec-2-21.html", {"schedule":schedule})
    
def IS_2_20(request):
    schedule = Schedule3.objects.all()[42:48]
    return render(request, "firstcourse/tdng-1-21.html", {"schedule":schedule})

def KIP_3_20(request):
    schedule = Schedule3.objects.all()[48:54]
    return render(request, "firstcourse/xtp-11-21.html", {"schedule":schedule})

def KIP_4_20(request):
    schedule = Schedule3.objects.all()[54:60]
    return render(request, "firstcourse/xtp-1-21.html", {"schedule":schedule})

def KIP_11_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "firstcourse/aiy-1-21.html", {"schedule":schedule})

def XTP_1_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "firstcourse/aiy-1-21.html", {"schedule":schedule})

def XTP_2_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "firstcourse/aiy-1-21.html", {"schedule":schedule})

def XTP_3_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "firstcourse/aiy-1-21.html", {"schedule":schedule}) 