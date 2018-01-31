# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserProfile(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    result = models.IntegerField(null = True)

    def __str__(self):
        return self.user

class Question(models.Model):
    text = models.TextField(max_length = 500)
    order_no = models.IntegerField()
    correct_choice = models.OneToOneField("Question_Choice", related_name = "question_cc", null = True)

    def __str__(self):
        return self.text

class Question_Choice(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length = 200)

    def __str__(self):
        return self.text

class User_Choice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.OneToOneField(Question)
    choice = models.OneToOneField(Question_Choice)
    iscorrect = models.BooleanField(default = 'False')

    def __str__(self):
        return "{} : {}".format(self.user, self.choice)
