# Generated by Django 4.2.6 on 2023-10-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=250, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('completion_date', models.DateField()),
            ],
        ),
    ]
