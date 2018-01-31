from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Question, User_Choice, UserProfile

@receiver(post_save, sender = User)
def create_userprofile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        userprofile = UserProfile(user = user)
        userprofile.save()

@receiver(post_save, sender = User)
def create_user_choices(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        question_list = Question.objects.all()
        for question in question_list:
            user_choice = User_Choice(user = user, question = question)
            user_choice.save()
