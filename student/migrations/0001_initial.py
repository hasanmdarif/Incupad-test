# Generated by Django 3.2 on 2022-02-28 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='markList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('studentName', models.CharField(max_length=100)),
                ('courseName', models.CharField(max_length=100)),
                ('marks', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('guardianName', models.CharField(max_length=100)),
            ],
        ),
    ]
