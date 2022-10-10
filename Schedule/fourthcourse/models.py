from django.db import models

# Create your models here.
class Schedule4(models.Model):

    choice_day = {
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
    }

    group = models.CharField('Group', max_length=100, default='Group name')

    lesson = models.CharField('Lesson', max_length=10, default='lesson')

    monday = models.CharField('Monday', max_length=100, default='Monday')
    teacher_room1 = models.CharField("Учитель", max_length=100, default='teacher')

    tuesday = models.CharField('Tuesday', max_length=100, default='Tuesday')
    teacher_room2 = models.CharField("Учитель", max_length=100, default='teacher')

    wednesday = models.CharField('Wednesday', max_length=100, default='Wednesday')
    teacher_room3 = models.CharField("Учитель", max_length=100, default='teacher')

    thursday = models.CharField('Thursday', max_length=100, default='Thursday')
    teacher_room4 = models.CharField("Учитель", max_length=100, default='teacher')

    friday = models.CharField('Friday', max_length=100, default='Friday')
    teacher_room5 = models.CharField("Учитель", max_length=100, default='teacher')

    time = models.CharField('time', max_length=100, default='Time')

    day = models.CharField('date', max_length=100, default='Date')

# from django.db import models




# # Create your models here.
# class Schedule1(models.Model):

#     choice_day = {
#         ('monday', 'monday'),
#         ('tuesday', 'tuesday'),
#         ('wednesday', 'wednesday'),
#         ('thursday', 'thursday'),
#         ('friday', 'friday'),
#     }

#     group = models.CharField('Group', max_length=100, default='Group name')

#     lesson = models.CharField('Lesson', max_length=10, default='lesson')

#     monday = models.CharField('Monday', max_length=100, default='Monday')
#     teacher_room1 = models.CharField("Учитель", max_length=100, default='teacher')

#     tuesday = models.CharField('Tuesday', max_length=100, default='Tuesday')
#     teacher_room2 = models.CharField("Учитель", max_length=100, default='teacher')

#     wednesday = models.CharField('Wednesday', max_length=100, default='Wednesday')
#     teacher_room3 = models.CharField("Учитель", max_length=100, default='teacher')

#     thursday = models.CharField('Thursday', max_length=100, default='Thursday')
#     teacher_room4 = models.CharField("Учитель", max_length=100, default='teacher')

#     friday = models.CharField('Friday', max_length=100, default='Friday')
#     teacher_room5 = models.CharField("Учитель", max_length=100, default='teacher')

#     time = models.CharField('time', max_length=100, default='Time')

