# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=10)),
                ('postal', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=50)),
                ('token', models.CharField(blank=True, max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager', models.BooleanField()),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='household.Household')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='household',
            name='residents',
            field=models.ManyToManyField(through='household.Resident', to=settings.AUTH_USER_MODEL),
        ),
    ]
