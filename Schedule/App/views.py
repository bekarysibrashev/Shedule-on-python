from django.shortcuts import render
# from .models import Schedule1

# Главная страница

def index(request):

    return render(request, "App/index.html")


# Выбор курса

def first_course(request):
    
    return render(request, "App/1 course.html")

def second_course(request):
    # schedule = Schedule.objects.all()
    return render(request, "App/2 course.html")

def third_course(request):
    
    return render(request, "App/3 course.html")

def fourth_course(request):
 
    return render(request, "App/4 course.html")


# Выбор группы


# def "(request):
#     schedule = Schedule.objects.all()[:5]
#     return render(request, "App/po-1-21.html", {"schedule":schedule})