from django.shortcuts import render
from .models import Schedule4
# Create your views here.


def index(request):
    return render(request, "App/index.html")



def AIY_1_19(request):
    schedule = Schedule4.objects.all()[:6]
    return render(request, "fourthcourse/aiy-1-19.html", {"schedule":schedule})

def AIY_2_19(request):
    schedule = Schedule4.objects.all()[6:12]
    return render(request, "fourthcourse/aiy-2-19.html", {"schedule":schedule})

def BNGS_1_19(request):
    schedule = Schedule4.objects.all()[12:18]
    return render(request, "fourthcourse/bngs-1-19.html", {"schedule":schedule})
    
def ES_1_19(request):
    schedule = Schedule4.objects.all()[18:24]
    return render(request, "fourthcourse/ec-1-19.html", {"schedule":schedule})

def ES_2_19(request):
    schedule = Schedule4.objects.all()[24:30]
    return render(request, "fourthcourse/ec-2-19.html", {"schedule":schedule})


def ES_3_19(request):
    schedule = Schedule4.objects.all()[30:36]
    return render(request, "fourthcourse/ec-3-19.html", {"schedule":schedule})

def ES_4_19(request):
    schedule = Schedule4.objects.all()[36:42]
    return render(request, "fourthcourse/ec-4-19.html", {"schedule":schedule})

def ENGM_1_19(request):
    schedule = Schedule4.objects.all()[42:48]
    return render(request, "fourthcourse/engm-1-19.html", {"schedule":schedule})
    
def ENGM_2_19(request):
    schedule = Schedule4.objects.all()[48:54]
    return render(request, "fourthcourse/engm-2-19.html", {"schedule":schedule})

def ENGM_3_19(request):
    schedule = Schedule4.objects.all()[54:60]
    return render(request, "fourthcourse/engm-3-19.html", {"schedule":schedule})

def IS_1_19(request):
    schedule = Schedule4.objects.all()[60:66]
    return render(request, "fourthcourse/is-1-19.html", {"schedule":schedule})

def IS_2_19(request):
    schedule = Schedule4.objects.all()[66:72]
    return render(request, "fourthcourse/is-2-19.html", {"schedule":schedule})

def KIP_1_19(request):
    schedule = Schedule4.objects.all()[72:78]
    return render(request, "fourthcourse/kip-1-19.html", {"schedule":schedule})

def KIP_2_19(request):
    schedule = Schedule4.objects.all()[78:84]
    return render(request, "fourthcourse/kip-2-19.html", {"schedule":schedule})

def KIP_3_19(request):
    schedule = Schedule4.objects.all()[84:90]
    return render(request, "fourthcourse/kip-3-19.html", {"schedule":schedule})

def KIP_4_19(request):
    schedule = Schedule4.objects.all()[90:96]
    return render(request, "fourthcourse/kip-4-19.html", {"schedule":schedule})

def TDNG_1_19(request):
    schedule = Schedule4.objects.all()[96:102]
    return render(request, "fourthcourse/tdng-1-19.html", {"schedule":schedule})

def TXI_1_19(request):
    schedule = Schedule4.objects.all()[102:108]
    return render(request, "fourthcourse/txi-1-19.html", {"schedule":schedule})

def TXI_2_19(request):
    schedule = Schedule4.objects.all()[108:114]
    return render(request, "fourthcourse/txi-2-19.html", {"schedule":schedule})

def TXI_3_19(request):
    schedule = Schedule4.objects.all()[114:120]
    return render(request, "fourthcourse/txi-3-19.html", {"schedule":schedule})
