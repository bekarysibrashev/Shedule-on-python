# Generated by Django 4.1.1 on 2022-10-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_schedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.DateField(verbose_name='Data'),
        ),
    ]