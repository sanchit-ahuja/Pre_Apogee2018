# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-31 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180131_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_cc', to='quiz.Question_Choice'),
        ),
    ]
