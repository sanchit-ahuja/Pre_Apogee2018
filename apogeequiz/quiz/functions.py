from django.contrib.auth.models import User
from .models import User_Choice

def update_user_choice(user_choice):
    correct_choice = user_choice.question.correct_choice

    if (user_choice.choice == correct_choice):
        user_choice.iscorrect = 'True'
        user_choice.user.userprofile_set.result += 1
