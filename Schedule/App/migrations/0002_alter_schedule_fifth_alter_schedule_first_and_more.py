# Generated by Django 4.1.1 on 2022-10-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='fifth',
            field=models.CharField(default='some_value', max_length=150, verbose_name='5 урок'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='first',
            field=models.CharField(default='some_value', max_length=150, verbose_name='1 урок'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='fourth',
            field=models.CharField(default='some_value', max_length=150, verbose_name='4 урок'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='second',
            field=models.CharField(default='some_value', max_length=150, verbose_name='2 урок'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sixth',
            field=models.CharField(default='some_value', max_length=150, verbose_name='6 урок'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='third',
            field=models.CharField(default='some_value', max_length=150, verbose_name='3 урок'),
        ),
    ]
