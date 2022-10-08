# Generated by Django 4.1.1 on 2022-10-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=150, verbose_name='1 урок')),
                ('second', models.CharField(max_length=150, verbose_name='2 урок')),
                ('third', models.CharField(max_length=150, verbose_name='3 урок')),
                ('fourth', models.CharField(max_length=150, verbose_name='4 урок')),
                ('fifth', models.CharField(max_length=150, verbose_name='5 урок')),
                ('sixth', models.CharField(max_length=150, verbose_name='6 урок')),
            ],
        ),
    ]
