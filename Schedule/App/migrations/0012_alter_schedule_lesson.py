# Generated by Django 4.1.1 on 2022-10-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_remove_schedule_day_remove_schedule_fifth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='lesson',
            field=models.CharField(default='lesson', max_length=10, verbose_name='Lesson'),
        ),
    ]
