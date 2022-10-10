from django.shortcuts import render
from .models import Schedule3
# Create your views here.


def index(request):
    return render(request, "App/index.html")



def AIY_1_20(request):
    schedule = Schedule3.objects.all()[:6]
    return render(request, "thirdcourse/aiy-1-20.html", {"schedule":schedule})

def BNGS_1_20(request):
    schedule = Schedule3.objects.all()[6:12]
    return render(request, "thirdcourse/bngs-1-20.html", {"schedule":schedule})

def ES_1_20(request):
    schedule = Schedule3.objects.all()[12:18]
    return render(request, "thirdcourse/ec-1-20.html", {"schedule":schedule})
    
def ES_2_20(request):
    schedule = Schedule3.objects.all()[18:24]
    return render(request, "thirdcourse/ec-2-20.html", {"schedule":schedule})

def ES_3_20(request):
    schedule = Schedule3.objects.all()[24:30]
    return render(request, "thirdcourse/ec-1-20.html", {"schedule":schedule})

def ENGM_1_20(request):
    schedule = Schedule3.objects.all()[30:36]
    return render(request, "thirdcourse/engm-1-20.html", {"schedule":schedule})

def IS_1_20(request):
    schedule = Schedule3.objects.all()[36:42]
    return render(request, "thirdcourse/is-1-20.html", {"schedule":schedule})
    
def IS_2_20(request):
    schedule = Schedule3.objects.all()[42:48]
    return render(request, "thirdcourse/is-2-20.html", {"schedule":schedule})

def KIP_3_20(request):
    schedule = Schedule3.objects.all()[48:54]
    return render(request, "thirdcourse/kip-3-20.html", {"schedule":schedule})

def KIP_4_20(request):
    schedule = Schedule3.objects.all()[54:60]
    return render(request, "thirdcourse/kip-4-20.html", {"schedule":schedule})

def KIP_11_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "thirdcourse/kip-11-20.html", {"schedule":schedule})

def TXI_1_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "thirdcourse/txi-1-20.html", {"schedule":schedule})

def TXI_2_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "thirdcourse/txi-2-20.html", {"schedule":schedule})

def TXI_3_20(request):
    schedule = Schedule3.objects.all()[60:66]
    return render(request, "thirdcourse/txi-3-20.html", {"schedule":schedule}) 

def ENGM_2_20(request):
    schedule = Schedule3.objects.all()[66:72]
    return render(request, "thirdcourse/engm-2-20.html", {"schedule":schedule}) 

def TDNG_1_20(request):
    schedule = Schedule3.objects.all()[72:78]
    return render(request, "thirdcourse/engm-2-20.html", {"schedule":schedule}) 

def KIP_2_20(request):
    schedule = Schedule3.objects.all()[78:84]
    return render(request, "thirdcourse/engm-2-20.html", {"schedule":schedule}) 

def KIP_1_20(request):
    schedule = Schedule3.objects.all()[84:90]
    return render(request, "thirdcourse/engm-2-20.html", {"schedule":schedule}) 