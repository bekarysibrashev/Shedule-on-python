# Generated by Django 4.1.1 on 2022-10-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_schedule_fifth_alter_schedule_first_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.CharField(default='день недели', max_length=150, verbose_name='День'),
        ),
    ]