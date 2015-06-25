# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=30)),
                ('company_description', models.CharField(max_length=200)),
                ('company_address', models.CharField(max_length=50)),
                ('company_number', models.CharField(max_length=20)),
                ('company_contact_person', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_fname', models.CharField(max_length=20)),
                ('employee_mname', models.CharField(max_length=20)),
                ('employee_lname', models.CharField(max_length=20)),
                ('employee_sname', models.CharField(max_length=5)),
                ('employee_description', models.CharField(max_length=200)),
            ],
        ),
    ]
