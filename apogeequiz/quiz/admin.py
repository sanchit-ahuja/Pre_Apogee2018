from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Question, Question_Choice, User_Choice


# Inline admin descriptor for User_Choice model
class User_ChoiceInline(admin.StackedInline):
    model = User_Choice
    can_delete = False
    verbose_name_plural = 'choice'

# New User admin
class UserAdmin(BaseUserAdmin):
    inlines = (User_ChoiceInline, )

# Inline admin descriptor for Question_Choice model
class Question_ChoiceInline(admin.StackedInline):
    model = Question_Choice
    can_delete = True
    verbose_name_plural = 'choice'

#New Question admin
class QuestionAdmin(admin.ModelAdmin):
    fields = ['order_no', 'text', 'correct_choice']
    inlines = (Question_ChoiceInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#Register QuestionAdmin
admin.site.register(Question, QuestionAdmin)
